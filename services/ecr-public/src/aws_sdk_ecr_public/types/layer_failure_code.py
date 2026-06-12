"""Generated from Smithy shape ``com.amazonaws.ecrpublic#LayerFailureCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr_public.errors import DeserializationError

LayerFailureCode: TypeAlias = Literal[
    "InvalidLayerDigest",
    "MissingLayerDigest",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InvalidLayerDigest",
        "MissingLayerDigest",
    )
)


def serialize_aws_json_1_1(value: LayerFailureCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LayerFailureCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LayerFailureCode value: {data!r}")
    return cast(LayerFailureCode, data)
