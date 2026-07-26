"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CreateLinkResponse``."""

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
    import capo_rtbfabric.types.module_configuration_list


class CreateLinkResponse(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    peer_gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the peer gateway.</p>"""
    status: "capo_rtbfabric.types.link_status.LinkStatus"
    """<p>The status of the request.</p>"""
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
    connectivity_type: NotRequired[
        "capo_rtbfabric.types.connectivity_type.ConnectivityType"
    ]
    """<p>The connectivity type of the link.</p>"""
    link_id: "capo_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    customer_provided_id: NotRequired["str"]
    """<p>The customer-provided unique identifier of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLinkResponse) -> dict:
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
    if "customer_provided_id" in value:
        out["customerProvidedId"] = value["customer_provided_id"]
    return out


def deserialize_json(data: dict) -> CreateLinkResponse:
    out: CreateLinkResponse = {}  # type: ignore[typeddict-item]
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("CreateLinkResponse.gateway_id required")
    if "peerGatewayId" in data:
        out["peer_gateway_id"] = data["peerGatewayId"]
    else:
        raise DeserializationError("CreateLinkResponse.peer_gateway_id required")
    if "status" in data:
        import capo_rtbfabric.types.link_status

        out["status"] = capo_rtbfabric.types.link_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateLinkResponse.status required")
    if "createdAt" in data:
        import capo_rtbfabric.types._prelude.timestamp

        out["created_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("CreateLinkResponse.created_at required")
    if "updatedAt" in data:
        import capo_rtbfabric.types._prelude.timestamp

        out["updated_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("CreateLinkResponse.updated_at required")
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
        raise DeserializationError("CreateLinkResponse.link_id required")
    if "customerProvidedId" in data:
        out["customer_provided_id"] = data["customerProvidedId"]
    return out
