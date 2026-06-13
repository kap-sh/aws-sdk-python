"""Generated from Smithy shape ``com.amazonaws.quicksight#DatasetParameterValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

"""<p>The value type of the parameter. The value type is used to validate the parameter before it is evaluated.</p>"""
DatasetParameterValueType: TypeAlias = Literal[
    "MULTI_VALUED",
    "SINGLE_VALUED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MULTI_VALUED",
        "SINGLE_VALUED",
    )
)


def serialize_json(value: DatasetParameterValueType) -> str:
    return value


def deserialize_json(data: str) -> DatasetParameterValueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasetParameterValueType value: {data!r}")
    return cast(DatasetParameterValueType, data)
