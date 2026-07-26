"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_flow_category

MetaFlowCategoryList: TypeAlias = list[
    "capo_socialmessaging.types.meta_flow_category.MetaFlowCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowCategoryList) -> list:
    import capo_socialmessaging.types.meta_flow_category

    out: list = []
    for item in value:
        out.append(capo_socialmessaging.types.meta_flow_category.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetaFlowCategoryList:
    import capo_socialmessaging.types.meta_flow_category

    out: MetaFlowCategoryList = []
    for item in data:
        out.append(capo_socialmessaging.types.meta_flow_category.deserialize_json(item))
    return out
