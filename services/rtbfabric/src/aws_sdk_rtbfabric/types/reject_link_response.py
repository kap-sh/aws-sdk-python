"""Generated from Smithy shape ``com.amazonaws.rtbfabric#RejectLinkResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_rtbfabric.types.connectivity_type
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.link_attributes
    import aws_sdk_rtbfabric.types.link_direction
    import aws_sdk_rtbfabric.types.link_id
    import aws_sdk_rtbfabric.types.link_log_settings
    import aws_sdk_rtbfabric.types.link_status
    import aws_sdk_rtbfabric.types.module_configuration_list


class RejectLinkResponse(TypedDict):
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    peer_gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the peer gateway.</p>"""
    status: "aws_sdk_rtbfabric.types.link_status.LinkStatus"
    """<p>The status of the link.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp of when the link was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp of when the link was updated.</p>"""
    direction: NotRequired["aws_sdk_rtbfabric.types.link_direction.LinkDirection"]
    """<p>The direction of the link.</p>"""
    flow_modules: NotRequired[
        "aws_sdk_rtbfabric.types.module_configuration_list.ModuleConfigurationList"
    ]
    """<p>The configuration of flow modules.</p>"""
    pending_flow_modules: NotRequired[
        "aws_sdk_rtbfabric.types.module_configuration_list.ModuleConfigurationList"
    ]
    """<p>The configuration of pending flow modules.</p>"""
    attributes: NotRequired["aws_sdk_rtbfabric.types.link_attributes.LinkAttributes"]
    """<p>Attributes of the link.</p>"""
    log_settings: NotRequired[
        "aws_sdk_rtbfabric.types.link_log_settings.LinkLogSettings"
    ]
    connectivity_type: NotRequired[
        "aws_sdk_rtbfabric.types.connectivity_type.ConnectivityType"
    ]
    """<p>The connectivity type of the link.</p>"""
    link_id: "aws_sdk_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectLinkResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["peerGatewayId"] = value["peer_gateway_id"]
    import aws_sdk_rtbfabric.types.link_status

    out["status"] = aws_sdk_rtbfabric.types.link_status.serialize_json(value["status"])
    import aws_sdk_rtbfabric.types._prelude.timestamp

    out["createdAt"] = aws_sdk_rtbfabric.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_rtbfabric.types._prelude.timestamp

    out["updatedAt"] = aws_sdk_rtbfabric.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    if "direction" in value:
        import aws_sdk_rtbfabric.types.link_direction

        out["direction"] = aws_sdk_rtbfabric.types.link_direction.serialize_json(
            value["direction"]
        )
    if "flow_modules" in value:
        import aws_sdk_rtbfabric.types.module_configuration_list

        out["flowModules"] = (
            aws_sdk_rtbfabric.types.module_configuration_list.serialize_json(
                value["flow_modules"]
            )
        )
    if "pending_flow_modules" in value:
        import aws_sdk_rtbfabric.types.module_configuration_list

        out["pendingFlowModules"] = (
            aws_sdk_rtbfabric.types.module_configuration_list.serialize_json(
                value["pending_flow_modules"]
            )
        )
    if "attributes" in value:
        import aws_sdk_rtbfabric.types.link_attributes

        out["attributes"] = aws_sdk_rtbfabric.types.link_attributes.serialize_json(
            value["attributes"]
        )
    if "log_settings" in value:
        import aws_sdk_rtbfabric.types.link_log_settings

        out["logSettings"] = aws_sdk_rtbfabric.types.link_log_settings.serialize_json(
            value["log_settings"]
        )
    if "connectivity_type" in value:
        import aws_sdk_rtbfabric.types.connectivity_type

        out["connectivityType"] = (
            aws_sdk_rtbfabric.types.connectivity_type.serialize_json(
                value["connectivity_type"]
            )
        )
    out["linkId"] = value["link_id"]
    return out


def deserialize_json(data: dict) -> RejectLinkResponse:
    out: RejectLinkResponse = {}  # type: ignore[typeddict-item]
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("RejectLinkResponse.gateway_id required")
    if "peerGatewayId" in data:
        out["peer_gateway_id"] = data["peerGatewayId"]
    else:
        raise DeserializationError("RejectLinkResponse.peer_gateway_id required")
    if "status" in data:
        import aws_sdk_rtbfabric.types.link_status

        out["status"] = aws_sdk_rtbfabric.types.link_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("RejectLinkResponse.status required")
    if "createdAt" in data:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["created_at"] = aws_sdk_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("RejectLinkResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["updated_at"] = aws_sdk_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("RejectLinkResponse.updated_at required")
    if "direction" in data:
        import aws_sdk_rtbfabric.types.link_direction

        out["direction"] = aws_sdk_rtbfabric.types.link_direction.deserialize_json(
            data["direction"]
        )
    if "flowModules" in data:
        import aws_sdk_rtbfabric.types.module_configuration_list

        out["flow_modules"] = (
            aws_sdk_rtbfabric.types.module_configuration_list.deserialize_json(
                data["flowModules"]
            )
        )
    if "pendingFlowModules" in data:
        import aws_sdk_rtbfabric.types.module_configuration_list

        out["pending_flow_modules"] = (
            aws_sdk_rtbfabric.types.module_configuration_list.deserialize_json(
                data["pendingFlowModules"]
            )
        )
    if "attributes" in data:
        import aws_sdk_rtbfabric.types.link_attributes

        out["attributes"] = aws_sdk_rtbfabric.types.link_attributes.deserialize_json(
            data["attributes"]
        )
    if "logSettings" in data:
        import aws_sdk_rtbfabric.types.link_log_settings

        out["log_settings"] = (
            aws_sdk_rtbfabric.types.link_log_settings.deserialize_json(
                data["logSettings"]
            )
        )
    if "connectivityType" in data:
        import aws_sdk_rtbfabric.types.connectivity_type

        out["connectivity_type"] = (
            aws_sdk_rtbfabric.types.connectivity_type.deserialize_json(
                data["connectivityType"]
            )
        )
    if "linkId" in data:
        out["link_id"] = data["linkId"]
    else:
        raise DeserializationError("RejectLinkResponse.link_id required")
    return out
