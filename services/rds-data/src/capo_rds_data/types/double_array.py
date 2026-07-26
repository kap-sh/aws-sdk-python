"""Generated from Smithy shape ``com.amazonaws.rdsdata#DoubleArray``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rds_data.types.boxed_double

DoubleArray: TypeAlias = list["capo_rds_data.types.boxed_double.BoxedDouble | None"]


# --- restJson1 ser/de ---
def serialize_json(value: DoubleArray) -> list:
    return list(value)


def deserialize_json(data: list) -> DoubleArray:
    return list(data)
