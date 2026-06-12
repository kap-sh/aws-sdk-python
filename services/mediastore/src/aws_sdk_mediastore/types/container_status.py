"""Generated from Smithy shape ``com.amazonaws.mediastore#ContainerStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediastore.errors import DeserializationError

ContainerStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATING",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "CREATING",
        "DELETING",
    )
)


def serialize_aws_json_1_1(value: ContainerStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerStatus value: {data!r}")
    return cast(ContainerStatus, data)
