"""Generated from Smithy shape ``com.amazonaws.connect#FlowModule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.flow_module_id
    import capo_connect.types.flow_module_type


class FlowModule(TypedDict, closed=True):
    type: NotRequired["capo_connect.types.flow_module_type.FlowModuleType"]
    """<p> Only Type we support is MCP. </p>"""
    flow_module_id: NotRequired["capo_connect.types.flow_module_id.FlowModuleId"]
    """<p> If of Flow Modules invocable as tool </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowModule) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_connect.types.flow_module_type

        out["Type"] = capo_connect.types.flow_module_type.serialize_json(value["type"])
    if "flow_module_id" in value:
        out["FlowModuleId"] = value["flow_module_id"]
    return out


def deserialize_json(data: dict) -> FlowModule:
    out: FlowModule = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_connect.types.flow_module_type

        out["type"] = capo_connect.types.flow_module_type.deserialize_json(data["Type"])
    if "FlowModuleId" in data:
        out["flow_module_id"] = data["FlowModuleId"]
    return out
