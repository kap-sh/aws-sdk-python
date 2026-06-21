"""Generated from Smithy shape ``com.amazonaws.kendra#SharePointVersion``."""

from typing import Literal, TypeAlias, cast

SharePointVersion: TypeAlias = Literal[
    "SHAREPOINT_2013",
    "SHAREPOINT_2016",
    "SHAREPOINT_ONLINE",
    "SHAREPOINT_2019",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SharePointVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SharePointVersion:
    return cast(SharePointVersion, data)
