"""Generated from Smithy shape ``com.amazonaws.ssmincidents#RelatedItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_incidents.types.related_item

RelatedItemList: TypeAlias = list["capo_ssm_incidents.types.related_item.RelatedItem"]


# --- restJson1 ser/de ---
def serialize_json(value: RelatedItemList) -> list:
    import capo_ssm_incidents.types.related_item

    out: list = []
    for item in value:
        out.append(capo_ssm_incidents.types.related_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> RelatedItemList:
    import capo_ssm_incidents.types.related_item

    out: RelatedItemList = []
    for item in data:
        out.append(capo_ssm_incidents.types.related_item.deserialize_json(item))
    return out
