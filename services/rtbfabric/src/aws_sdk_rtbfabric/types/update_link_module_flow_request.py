"""Generated from Smithy shape ``com.amazonaws.rtbfabric#UpdateLinkModuleFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.link_id
    import aws_sdk_rtbfabric.types.module_configuration_list


class UpdateLinkModuleFlowRequest(TypedDict, closed=True):
    client_token: "str"
    """<p>The unique client token.</p>"""
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "aws_sdk_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    modules: "aws_sdk_rtbfabric.types.module_configuration_list.ModuleConfigurationList"
    """<p>The configuration of a module.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLinkModuleFlowRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    import aws_sdk_rtbfabric.types.module_configuration_list

    out["modules"] = aws_sdk_rtbfabric.types.module_configuration_list.serialize_json(
        value["modules"]
    )
    return out


def deserialize_json(data: dict) -> UpdateLinkModuleFlowRequest:
    out: UpdateLinkModuleFlowRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("UpdateLinkModuleFlowRequest.client_token required")
    if "modules" in data:
        import aws_sdk_rtbfabric.types.module_configuration_list

        out["modules"] = (
            aws_sdk_rtbfabric.types.module_configuration_list.deserialize_json(
                data["modules"]
            )
        )
    else:
        raise DeserializationError("UpdateLinkModuleFlowRequest.modules required")
    return out
