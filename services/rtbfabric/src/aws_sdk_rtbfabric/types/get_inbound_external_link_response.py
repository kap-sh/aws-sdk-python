"""Generated from Smithy shape ``com.amazonaws.rtbfabric#GetInboundExternalLinkResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_rtbfabric.types.connectivity_type
    import aws_sdk_rtbfabric.types.domain_name
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.link_attributes
    import aws_sdk_rtbfabric.types.link_id
    import aws_sdk_rtbfabric.types.link_log_settings
    import aws_sdk_rtbfabric.types.link_status
    import aws_sdk_rtbfabric.types.module_configuration_list
    import aws_sdk_rtbfabric.types.tags_map


class GetInboundExternalLinkResponse(TypedDict):
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "aws_sdk_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    status: "aws_sdk_rtbfabric.types.link_status.LinkStatus"
    """<p>The status of the request.</p>"""
    domain_name: "aws_sdk_rtbfabric.types.domain_name.DomainName"
    """<p>The domain name.</p>"""
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
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the inbound external link was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the inbound external link was updated.</p>"""
    tags: NotRequired["aws_sdk_rtbfabric.types.tags_map.TagsMap"]
    """<p>A map of the key-value pairs for the tag or tags assigned to the specified resource.</p>"""
    log_settings: NotRequired[
        "aws_sdk_rtbfabric.types.link_log_settings.LinkLogSettings"
    ]
    """<p>Settings for the application logs.</p>"""
    connectivity_type: NotRequired[
        "aws_sdk_rtbfabric.types.connectivity_type.ConnectivityType"
    ]
    """<p>The connectivity type of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInboundExternalLinkResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["linkId"] = value["link_id"]
    import aws_sdk_rtbfabric.types.link_status

    out["status"] = aws_sdk_rtbfabric.types.link_status.serialize_json(value["status"])
    out["domainName"] = value["domain_name"]
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
    if "created_at" in value:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["createdAt"] = aws_sdk_rtbfabric.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["updatedAt"] = aws_sdk_rtbfabric.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "tags" in value:
        import aws_sdk_rtbfabric.types.tags_map

        out["tags"] = aws_sdk_rtbfabric.types.tags_map.serialize_json(value["tags"])
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
    return out


def deserialize_json(data: dict) -> GetInboundExternalLinkResponse:
    out: GetInboundExternalLinkResponse = {}  # type: ignore[typeddict-item]
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("GetInboundExternalLinkResponse.gateway_id required")
    if "linkId" in data:
        out["link_id"] = data["linkId"]
    else:
        raise DeserializationError("GetInboundExternalLinkResponse.link_id required")
    if "status" in data:
        import aws_sdk_rtbfabric.types.link_status

        out["status"] = aws_sdk_rtbfabric.types.link_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetInboundExternalLinkResponse.status required")
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError(
            "GetInboundExternalLinkResponse.domain_name required"
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
    if "createdAt" in data:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["created_at"] = aws_sdk_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["updated_at"] = aws_sdk_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "tags" in data:
        import aws_sdk_rtbfabric.types.tags_map

        out["tags"] = aws_sdk_rtbfabric.types.tags_map.deserialize_json(data["tags"])
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
    return out
