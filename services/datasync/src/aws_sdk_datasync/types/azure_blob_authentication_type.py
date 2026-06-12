"""Generated from Smithy shape ``com.amazonaws.datasync#AzureBlobAuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

AzureBlobAuthenticationType: TypeAlias = Literal[
    "SAS",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SAS",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: AzureBlobAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AzureBlobAuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AzureBlobAuthenticationType value: {data!r}"
        )
    return cast(AzureBlobAuthenticationType, data)
