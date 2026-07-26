"""Generated from Smithy shape ``com.amazonaws.rtbfabric#GetLinkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_rtbfabric.types.connectivity_type
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.link_attributes
    import capo_rtbfabric.types.link_direction
    import capo_rtbfabric.types.link_id
    import capo_rtbfabric.types.link_log_settings
    import capo_rtbfabric.types.link_status
    import capo_rtbfabric.types.link_timeout_in_millis
    import capo_rtbfabric.types.module_configuration_list
    import capo_rtbfabric.types.tags_map


class GetLinkResponse(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    peer_gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the peer gateway.</p>"""
    status: "capo_rtbfabric.types.link_status.LinkStatus"
    """<p>The status of the link.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp of when the link was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp of when the link was updated.</p>"""
    direction: NotRequired["capo_rtbfabric.types.link_direction.LinkDirection"]
    """<p>The direction of the link.</p>"""
    flow_modules: NotRequired[
        "capo_rtbfabric.types.module_configuration_list.ModuleConfigurationList"
    ]
    """<p>The configuration of flow modules.</p>"""
    pending_flow_modules: NotRequired[
        "capo_rtbfabric.types.module_configuration_list.ModuleConfigurationList"
    ]
    """<p>The configuration of pending flow modules.</p>"""
    attributes: NotRequired["capo_rtbfabric.types.link_attributes.LinkAttributes"]
    """<p>Attributes of the link.</p>"""
    log_settings: NotRequired["capo_rtbfabric.types.link_log_settings.LinkLogSettings"]
    """<p>Settings for the application logs.</p>"""
    connectivity_type: NotRequired[
        "capo_rtbfabric.types.connectivity_type.ConnectivityType"
    ]
    """<p>The connectivity type of the link.</p>"""
    link_id: "capo_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    tags: NotRequired["capo_rtbfabric.types.tags_map.TagsMap"]
    """<p>A map of the key-value pairs for the tag or tags assigned to the specified resource.</p>"""
    http_responder_allowed: NotRequired["bool"]
    """<p>Boolean to specify if an HTTP responder is allowed.</p>"""
    timeout_in_millis: NotRequired[
        "capo_rtbfabric.types.link_timeout_in_millis.LinkTimeoutInMillis"
    ]
    """<p>The timeout value in milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLinkResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["peerGatewayId"] = value["peer_gateway_id"]
    import capo_rtbfabric.types.link_status

    out["status"] = capo_rtbfabric.types.link_status.serialize_json(value["status"])
    import capo_rtbfabric.types._prelude.timestamp

    out["createdAt"] = capo_rtbfabric.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_rtbfabric.types._prelude.timestamp

    out["updatedAt"] = capo_rtbfabric.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    if "direction" in value:
        import capo_rtbfabric.types.link_direction

        out["direction"] = capo_rtbfabric.types.link_direction.serialize_json(
            value["direction"]
        )
    if "flow_modules" in value:
        import capo_rtbfabric.types.module_configuration_list

        out["flowModules"] = (
            capo_rtbfabric.types.module_configuration_list.serialize_json(
                value["flow_modules"]
            )
        )
    if "pending_flow_modules" in value:
        import capo_rtbfabric.types.module_configuration_list

        out["pendingFlowModules"] = (
            capo_rtbfabric.types.module_configuration_list.serialize_json(
                value["pending_flow_modules"]
            )
        )
    if "attributes" in value:
        import capo_rtbfabric.types.link_attributes

        out["attributes"] = capo_rtbfabric.types.link_attributes.serialize_json(
            value["attributes"]
        )
    if "log_settings" in value:
        import capo_rtbfabric.types.link_log_settings

        out["logSettings"] = capo_rtbfabric.types.link_log_settings.serialize_json(
            value["log_settings"]
        )
    if "connectivity_type" in value:
        import capo_rtbfabric.types.connectivity_type

        out["connectivityType"] = capo_rtbfabric.types.connectivity_type.serialize_json(
            value["connectivity_type"]
        )
    out["linkId"] = value["link_id"]
    if "tags" in value:
        import capo_rtbfabric.types.tags_map

        out["tags"] = capo_rtbfabric.types.tags_map.serialize_json(value["tags"])
    if "http_responder_allowed" in value:
        out["httpResponderAllowed"] = value["http_responder_allowed"]
    if "timeout_in_millis" in value:
        out["timeoutInMillis"] = value["timeout_in_millis"]
    return out


def deserialize_json(data: dict) -> GetLinkResponse:
    out: GetLinkResponse = {}  # type: ignore[typeddict-item]
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("GetLinkResponse.gateway_id required")
    if "peerGatewayId" in data:
        out["peer_gateway_id"] = data["peerGatewayId"]
    else:
        raise DeserializationError("GetLinkResponse.peer_gateway_id required")
    if "status" in data:
        import capo_rtbfabric.types.link_status

        out["status"] = capo_rtbfabric.types.link_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetLinkResponse.status required")
    if "createdAt" in data:
        import capo_rtbfabric.types._prelude.timestamp

        out["created_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetLinkResponse.created_at required")
    if "updatedAt" in data:
        import capo_rtbfabric.types._prelude.timestamp

        out["updated_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("GetLinkResponse.updated_at required")
    if "direction" in data:
        import capo_rtbfabric.types.link_direction

        out["direction"] = capo_rtbfabric.types.link_direction.deserialize_json(
            data["direction"]
        )
    if "flowModules" in data:
        import capo_rtbfabric.types.module_configuration_list

        out["flow_modules"] = (
            capo_rtbfabric.types.module_configuration_list.deserialize_json(
                data["flowModules"]
            )
        )
    if "pendingFlowModules" in data:
        import capo_rtbfabric.types.module_configuration_list

        out["pending_flow_modules"] = (
            capo_rtbfabric.types.module_configuration_list.deserialize_json(
                data["pendingFlowModules"]
            )
        )
    if "attributes" in data:
        import capo_rtbfabric.types.link_attributes

        out["attributes"] = capo_rtbfabric.types.link_attributes.deserialize_json(
            data["attributes"]
        )
    if "logSettings" in data:
        import capo_rtbfabric.types.link_log_settings

        out["log_settings"] = capo_rtbfabric.types.link_log_settings.deserialize_json(
            data["logSettings"]
        )
    if "connectivityType" in data:
        import capo_rtbfabric.types.connectivity_type

        out["connectivity_type"] = (
            capo_rtbfabric.types.connectivity_type.deserialize_json(
                data["connectivityType"]
            )
        )
    if "linkId" in data:
        out["link_id"] = data["linkId"]
    else:
        raise DeserializationError("GetLinkResponse.link_id required")
    if "tags" in data:
        import capo_rtbfabric.types.tags_map

        out["tags"] = capo_rtbfabric.types.tags_map.deserialize_json(data["tags"])
    if "httpResponderAllowed" in data:
        out["http_responder_allowed"] = data["httpResponderAllowed"]
    if "timeoutInMillis" in data:
        out["timeout_in_millis"] = data["timeoutInMillis"]
    return out
