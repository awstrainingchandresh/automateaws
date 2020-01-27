import boto3
import click

session=boto3.Session(profile_name='default')
s3=session.resource('s3')

print("session started of s3 and you are access the S3 bucket from python")

@click.group()
def cli():
    "To get the info related to s3 buckets and objects(FILE)"
    pass


@cli.command("list-buckets")
def list_buckets():
    "To get the list of buckets in S3"
    print("Buckets in S3\n\n")
    for bucket in s3.buckets.all():
        print(bucket.name)

@cli.command("files-in-buckets")
@click.argument('bucketname')
def files_in_buckets(bucketname):
    "To get the list of files in bucket"
    print("List of file in Bucket "+ bucketname)
    print("\n")
    for files in s3.Bucket(bucketname).objects.all():
        print(files.key)
    print("\n\n")



if __name__=='__main__':
    cli()
