"""Generated from Smithy shape ``com.amazonaws.fsx#MetadataConfigurationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

MetadataConfigurationMode: TypeAlias = Literal[
    "AUTOMATIC",
    "USER_PROVISIONED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "USER_PROVISIONED",
    )
)


def serialize_aws_json_1_1(value: MetadataConfigurationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetadataConfigurationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetadataConfigurationMode value: {data!r}")
    return cast(MetadataConfigurationMode, data)
