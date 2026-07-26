"""Generated from Smithy shape ``com.amazonaws.mediatailor#RequestOutputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.request_output_item

RequestOutputs: TypeAlias = list[
    "capo_mediatailor.types.request_output_item.RequestOutputItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: RequestOutputs) -> list:
    import capo_mediatailor.types.request_output_item

    out: list = []
    for item in value:
        out.append(capo_mediatailor.types.request_output_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> RequestOutputs:
    import capo_mediatailor.types.request_output_item

    out: RequestOutputs = []
    for item in data:
        out.append(capo_mediatailor.types.request_output_item.deserialize_json(item))
    return out
