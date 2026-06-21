"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#AWSRegion``."""

from typing import Literal, TypeAlias, cast

"""<p>The region of the S3 bucket that Amazon Web Services delivers the report into.</p>"""
AWSRegion: TypeAlias = Literal[
    "af-south-1",
    "ap-east-1",
    "ap-south-1",
    "ap-south-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-southeast-3",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ca-central-1",
    "eu-central-1",
    "eu-central-2",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "eu-north-1",
    "eu-south-1",
    "eu-south-2",
    "me-central-1",
    "me-south-1",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
    "cn-north-1",
    "cn-northwest-1",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AWSRegion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AWSRegion:
    return cast(AWSRegion, data)
