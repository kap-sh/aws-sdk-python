"""Generated from Smithy shape ``com.amazonaws.connect#DescribeContactFlowModuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_module


class DescribeContactFlowModuleResponse(TypedDict, closed=True):
    contact_flow_module: NotRequired[
        "aws_sdk_connect.types.contact_flow_module.ContactFlowModule"
    ]
    """<p>Information about the flow module.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeContactFlowModuleResponse) -> dict:
    out: dict = {}
    if "contact_flow_module" in value:
        import aws_sdk_connect.types.contact_flow_module

        out["ContactFlowModule"] = (
            aws_sdk_connect.types.contact_flow_module.serialize_json(
                value["contact_flow_module"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeContactFlowModuleResponse:
    out: DescribeContactFlowModuleResponse = {}  # type: ignore[typeddict-item]
    if "ContactFlowModule" in data:
        import aws_sdk_connect.types.contact_flow_module

        out["contact_flow_module"] = (
            aws_sdk_connect.types.contact_flow_module.deserialize_json(
                data["ContactFlowModule"]
            )
        )
    return out
