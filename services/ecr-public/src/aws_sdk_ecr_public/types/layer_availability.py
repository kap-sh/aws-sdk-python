"""Generated from Smithy shape ``com.amazonaws.ecrpublic#LayerAvailability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr_public.errors import DeserializationError

LayerAvailability: TypeAlias = Literal[
    "AVAILABLE",
    "UNAVAILABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "UNAVAILABLE",
    )
)


def serialize_aws_json_1_1(value: LayerAvailability) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LayerAvailability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LayerAvailability value: {data!r}")
    return cast(LayerAvailability, data)
