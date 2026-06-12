"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointConfigSortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

EndpointConfigSortKey: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
    )
)


def serialize_aws_json_1_1(value: EndpointConfigSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointConfigSortKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointConfigSortKey value: {data!r}")
    return cast(EndpointConfigSortKey, data)
