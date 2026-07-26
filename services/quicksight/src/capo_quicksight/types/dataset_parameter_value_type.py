"""Generated from Smithy shape ``com.amazonaws.quicksight#DatasetParameterValueType``."""

from typing import Literal, TypeAlias, cast

"""<p>The value type of the parameter. The value type is used to validate the parameter before it is evaluated.</p>"""
DatasetParameterValueType: TypeAlias = Literal[
    "MULTI_VALUED",
    "SINGLE_VALUED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetParameterValueType) -> str:
    return value


def deserialize_json(data: str) -> DatasetParameterValueType:
    return cast(DatasetParameterValueType, data)
