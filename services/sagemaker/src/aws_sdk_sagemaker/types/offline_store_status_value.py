"""Generated from Smithy shape ``com.amazonaws.sagemaker#OfflineStoreStatusValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

OfflineStoreStatusValue: TypeAlias = Literal[
    "Active",
    "Blocked",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Blocked",
        "Disabled",
    )
)


def serialize_aws_json_1_1(value: OfflineStoreStatusValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OfflineStoreStatusValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OfflineStoreStatusValue value: {data!r}")
    return cast(OfflineStoreStatusValue, data)
