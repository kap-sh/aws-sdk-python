"""Generated from Smithy shape ``com.amazonaws.connect#MetricFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.string

MetricFilterValueList: TypeAlias = list["capo_connect.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: MetricFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> MetricFilterValueList:
    return list(data)
