"""Generated from Smithy shape ``com.amazonaws.athena#S3AclOption``."""

from typing import Literal, TypeAlias, cast

S3AclOption: TypeAlias = Literal["BUCKET_OWNER_FULL_CONTROL",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3AclOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3AclOption:
    return cast(S3AclOption, data)
