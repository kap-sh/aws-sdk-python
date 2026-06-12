"""Generated from Smithy shape ``com.amazonaws.kendra#SharePointVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

SharePointVersion: TypeAlias = Literal[
    "SHAREPOINT_2013",
    "SHAREPOINT_2016",
    "SHAREPOINT_ONLINE",
    "SHAREPOINT_2019",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHAREPOINT_2013",
        "SHAREPOINT_2016",
        "SHAREPOINT_ONLINE",
        "SHAREPOINT_2019",
    )
)


def serialize_aws_json_1_1(value: SharePointVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SharePointVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SharePointVersion value: {data!r}")
    return cast(SharePointVersion, data)
