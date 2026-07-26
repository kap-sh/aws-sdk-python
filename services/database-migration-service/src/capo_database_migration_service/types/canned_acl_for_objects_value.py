"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CannedAclForObjectsValue``."""

from typing import Literal, TypeAlias, cast

CannedAclForObjectsValue: TypeAlias = Literal[
    "none",
    "private",
    "public-read",
    "public-read-write",
    "authenticated-read",
    "aws-exec-read",
    "bucket-owner-read",
    "bucket-owner-full-control",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CannedAclForObjectsValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CannedAclForObjectsValue:
    return cast(CannedAclForObjectsValue, data)
