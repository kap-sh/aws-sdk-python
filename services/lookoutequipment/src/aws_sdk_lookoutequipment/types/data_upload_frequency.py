"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DataUploadFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lookoutequipment.errors import DeserializationError

DataUploadFrequency: TypeAlias = Literal[
    "PT5M",
    "PT10M",
    "PT15M",
    "PT30M",
    "PT1H",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PT5M",
        "PT10M",
        "PT15M",
        "PT30M",
        "PT1H",
    )
)


def serialize_aws_json_1_0(value: DataUploadFrequency) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DataUploadFrequency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataUploadFrequency value: {data!r}")
    return cast(DataUploadFrequency, data)
