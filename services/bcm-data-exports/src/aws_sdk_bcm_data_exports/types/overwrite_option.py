"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#OverwriteOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_data_exports.errors import DeserializationError

OverwriteOption: TypeAlias = Literal[
    "CREATE_NEW_REPORT",
    "OVERWRITE_REPORT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_NEW_REPORT",
        "OVERWRITE_REPORT",
    )
)


def serialize_aws_json_1_1(value: OverwriteOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OverwriteOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OverwriteOption value: {data!r}")
    return cast(OverwriteOption, data)
