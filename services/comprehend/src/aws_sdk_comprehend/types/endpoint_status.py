"""Generated from Smithy shape ``com.amazonaws.comprehend#EndpointStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

EndpointStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "FAILED",
    "IN_SERVICE",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "DELETING",
        "FAILED",
        "IN_SERVICE",
        "UPDATING",
    )
)


def serialize_aws_json_1_1(value: EndpointStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointStatus value: {data!r}")
    return cast(EndpointStatus, data)
