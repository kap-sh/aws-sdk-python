"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressionListReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.suppression_list_reason

SuppressionListReasons: TypeAlias = list[
    "capo_sesv2.types.suppression_list_reason.SuppressionListReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuppressionListReasons) -> list:
    import capo_sesv2.types.suppression_list_reason

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.suppression_list_reason.serialize_json(item))
    return out


def deserialize_json(data: list) -> SuppressionListReasons:
    import capo_sesv2.types.suppression_list_reason

    out: SuppressionListReasons = []
    for item in data:
        out.append(capo_sesv2.types.suppression_list_reason.deserialize_json(item))
    return out
