"""Generated from Smithy shape ``com.amazonaws.guardduty#Lineage``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.lineage_object

Lineage: TypeAlias = list["capo_guardduty.types.lineage_object.LineageObject"]


# --- restJson1 ser/de ---
def serialize_json(value: Lineage) -> list:
    import capo_guardduty.types.lineage_object

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.lineage_object.serialize_json(item))
    return out


def deserialize_json(data: list) -> Lineage:
    import capo_guardduty.types.lineage_object

    out: Lineage = []
    for item in data:
        out.append(capo_guardduty.types.lineage_object.deserialize_json(item))
    return out
