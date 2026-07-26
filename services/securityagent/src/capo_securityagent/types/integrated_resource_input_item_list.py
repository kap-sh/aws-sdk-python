"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegratedResourceInputItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.integrated_resource_input_item

IntegratedResourceInputItemList: TypeAlias = list[
    "capo_securityagent.types.integrated_resource_input_item.IntegratedResourceInputItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegratedResourceInputItemList) -> list:
    import capo_securityagent.types.integrated_resource_input_item

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.integrated_resource_input_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IntegratedResourceInputItemList:
    import capo_securityagent.types.integrated_resource_input_item

    out: IntegratedResourceInputItemList = []
    for item in data:
        out.append(
            capo_securityagent.types.integrated_resource_input_item.deserialize_json(
                item
            )
        )
    return out
