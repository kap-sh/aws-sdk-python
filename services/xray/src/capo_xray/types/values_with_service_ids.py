"""Generated from Smithy shape ``com.amazonaws.xray#ValuesWithServiceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.value_with_service_ids

ValuesWithServiceIds: TypeAlias = list[
    "capo_xray.types.value_with_service_ids.ValueWithServiceIds"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValuesWithServiceIds) -> list:
    import capo_xray.types.value_with_service_ids

    out: list = []
    for item in value:
        out.append(capo_xray.types.value_with_service_ids.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValuesWithServiceIds:
    import capo_xray.types.value_with_service_ids

    out: ValuesWithServiceIds = []
    for item in data:
        out.append(capo_xray.types.value_with_service_ids.deserialize_json(item))
    return out
