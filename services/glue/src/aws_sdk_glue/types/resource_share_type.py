"""Generated from Smithy shape ``com.amazonaws.glue#ResourceShareType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ResourceShareType: TypeAlias = Literal[
    "FOREIGN",
    "ALL",
    "FEDERATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FOREIGN",
        "ALL",
        "FEDERATED",
    )
)


def serialize_aws_json_1_1(value: ResourceShareType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceShareType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceShareType value: {data!r}")
    return cast(ResourceShareType, data)
