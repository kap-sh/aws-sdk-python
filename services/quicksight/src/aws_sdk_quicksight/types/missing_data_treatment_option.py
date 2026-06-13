"""Generated from Smithy shape ``com.amazonaws.quicksight#MissingDataTreatmentOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

MissingDataTreatmentOption: TypeAlias = Literal[
    "INTERPOLATE",
    "SHOW_AS_ZERO",
    "SHOW_AS_BLANK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERPOLATE",
        "SHOW_AS_ZERO",
        "SHOW_AS_BLANK",
    )
)


def serialize_json(value: MissingDataTreatmentOption) -> str:
    return value


def deserialize_json(data: str) -> MissingDataTreatmentOption:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MissingDataTreatmentOption value: {data!r}"
        )
    return cast(MissingDataTreatmentOption, data)
