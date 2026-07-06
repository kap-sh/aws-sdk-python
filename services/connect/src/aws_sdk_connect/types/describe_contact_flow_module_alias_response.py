"""Generated from Smithy shape ``com.amazonaws.connect#DescribeContactFlowModuleAliasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_module_alias_info


class DescribeContactFlowModuleAliasResponse(TypedDict, closed=True):
    contact_flow_module_alias: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_alias_info.ContactFlowModuleAliasInfo"
    ]
    """<p>Information about the flow module alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeContactFlowModuleAliasResponse) -> dict:
    out: dict = {}
    if "contact_flow_module_alias" in value:
        import aws_sdk_connect.types.contact_flow_module_alias_info

        out["ContactFlowModuleAlias"] = (
            aws_sdk_connect.types.contact_flow_module_alias_info.serialize_json(
                value["contact_flow_module_alias"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeContactFlowModuleAliasResponse:
    out: DescribeContactFlowModuleAliasResponse = {}  # type: ignore[typeddict-item]
    if "ContactFlowModuleAlias" in data:
        import aws_sdk_connect.types.contact_flow_module_alias_info

        out["contact_flow_module_alias"] = (
            aws_sdk_connect.types.contact_flow_module_alias_info.deserialize_json(
                data["ContactFlowModuleAlias"]
            )
        )
    return out
