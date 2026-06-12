"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointSortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

EndpointSortKey: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
        "Status",
    )
)


def serialize_aws_json_1_1(value: EndpointSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointSortKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointSortKey value: {data!r}")
    return cast(EndpointSortKey, data)
