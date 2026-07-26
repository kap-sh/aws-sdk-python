"""Generated from Smithy shape ``com.amazonaws.rtbfabric#FlowModuleNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rtbfabric.types.flow_module_name

FlowModuleNameList: TypeAlias = list[
    "capo_rtbfabric.types.flow_module_name.FlowModuleName"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowModuleNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> FlowModuleNameList:
    return list(data)
