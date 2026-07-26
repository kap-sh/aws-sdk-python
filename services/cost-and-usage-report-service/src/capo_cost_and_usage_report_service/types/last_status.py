"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#LastStatus``."""

from typing import Literal, TypeAlias, cast

LastStatus: TypeAlias = Literal[
    "SUCCESS",
    "ERROR_PERMISSIONS",
    "ERROR_NO_BUCKET",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LastStatus:
    return cast(LastStatus, data)
