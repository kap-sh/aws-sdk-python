"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CreatePortalResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048
    import aws_sdk_apigatewayv2.types.__string_min0_max255
    import aws_sdk_apigatewayv2.types.__string_min0_max1024
    import aws_sdk_apigatewayv2.types.__string_min10_max30_pattern_az09
    import aws_sdk_apigatewayv2.types.__string_min20_max2048
    import aws_sdk_apigatewayv2.types.__timestamp_iso8601
    import aws_sdk_apigatewayv2.types.authorization
    import aws_sdk_apigatewayv2.types.endpoint_configuration_response
    import aws_sdk_apigatewayv2.types.portal_content
    import aws_sdk_apigatewayv2.types.publish_status
    import aws_sdk_apigatewayv2.types.status_exception
    import aws_sdk_apigatewayv2.types.tags


class CreatePortalResponse(TypedDict):
    authorization: NotRequired["aws_sdk_apigatewayv2.types.authorization.Authorization"]
    """<p>The authorization for the portal. Supports Cognito-based user authentication or no authentication.</p>"""
    endpoint_configuration: NotRequired[
        "aws_sdk_apigatewayv2.types.endpoint_configuration_response.EndpointConfigurationResponse"
    ]
    """<p>The endpoint configuration.</p>"""
    included_portal_product_arns: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048.__listOf__stringMin20Max2048"
    ]
    """<p>The ARNs of the portal products included in the portal.</p>"""
    last_modified: NotRequired[
        "aws_sdk_apigatewayv2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The timestamp when the portal configuration was last modified.</p>"""
    last_published: NotRequired[
        "aws_sdk_apigatewayv2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The timestamp when the portal was last published.</p>"""
    last_published_description: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min0_max1024.__stringMin0Max1024"
    ]
    """<p>A user-written description of the changes made in the last published version of the portal.</p>"""
    portal_arn: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min20_max2048.__stringMin20Max2048"
    ]
    """<p>The ARN of the portal.</p>"""
    portal_content: NotRequired[
        "aws_sdk_apigatewayv2.types.portal_content.PortalContent"
    ]
    """<p>The name, description, and theme for the portal.</p>"""
    portal_id: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min10_max30_pattern_az09.__stringMin10Max30PatternAZ09"
    ]
    """<p>The portal identifier.</p>"""
    publish_status: NotRequired[
        "aws_sdk_apigatewayv2.types.publish_status.PublishStatus"
    ]
    """<p>The current publishing status of the portal.</p>"""
    rum_app_monitor_name: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min0_max255.__stringMin0Max255"
    ]
    """<p>The name of the Amazon CloudWatch RUM app monitor.</p>"""
    status_exception: NotRequired[
        "aws_sdk_apigatewayv2.types.status_exception.StatusException"
    ]
    """<p>Error information for failed portal operations. Contains details about any issues encountered during portal creation or publishing.</p>"""
    tags: NotRequired["aws_sdk_apigatewayv2.types.tags.Tags"]
    """<p>The collection of tags. Each tag element is associated with a given resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePortalResponse) -> dict:
    out: dict = {}
    if "authorization" in value:
        import aws_sdk_apigatewayv2.types.authorization

        out["authorization"] = aws_sdk_apigatewayv2.types.authorization.serialize_json(
            value["authorization"]
        )
    if "endpoint_configuration" in value:
        import aws_sdk_apigatewayv2.types.endpoint_configuration_response

        out["endpointConfiguration"] = (
            aws_sdk_apigatewayv2.types.endpoint_configuration_response.serialize_json(
                value["endpoint_configuration"]
            )
        )
    if "included_portal_product_arns" in value:
        import aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048

        out["includedPortalProductArns"] = (
            aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048.serialize_json(
                value["included_portal_product_arns"]
            )
        )
    if "last_modified" in value:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["lastModified"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.serialize_json(
                value["last_modified"]
            )
        )
    if "last_published" in value:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["lastPublished"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.serialize_json(
                value["last_published"]
            )
        )
    if "last_published_description" in value:
        out["lastPublishedDescription"] = value["last_published_description"]
    if "portal_arn" in value:
        out["portalArn"] = value["portal_arn"]
    if "portal_content" in value:
        import aws_sdk_apigatewayv2.types.portal_content

        out["portalContent"] = aws_sdk_apigatewayv2.types.portal_content.serialize_json(
            value["portal_content"]
        )
    if "portal_id" in value:
        out["portalId"] = value["portal_id"]
    if "publish_status" in value:
        import aws_sdk_apigatewayv2.types.publish_status

        out["publishStatus"] = aws_sdk_apigatewayv2.types.publish_status.serialize_json(
            value["publish_status"]
        )
    if "rum_app_monitor_name" in value:
        out["rumAppMonitorName"] = value["rum_app_monitor_name"]
    if "status_exception" in value:
        import aws_sdk_apigatewayv2.types.status_exception

        out["statusException"] = (
            aws_sdk_apigatewayv2.types.status_exception.serialize_json(
                value["status_exception"]
            )
        )
    if "tags" in value:
        import aws_sdk_apigatewayv2.types.tags

        out["tags"] = aws_sdk_apigatewayv2.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePortalResponse:
    out: CreatePortalResponse = {}  # type: ignore[typeddict-item]
    if "authorization" in data:
        import aws_sdk_apigatewayv2.types.authorization

        out["authorization"] = (
            aws_sdk_apigatewayv2.types.authorization.deserialize_json(
                data["authorization"]
            )
        )
    if "endpointConfiguration" in data:
        import aws_sdk_apigatewayv2.types.endpoint_configuration_response

        out["endpoint_configuration"] = (
            aws_sdk_apigatewayv2.types.endpoint_configuration_response.deserialize_json(
                data["endpointConfiguration"]
            )
        )
    if "includedPortalProductArns" in data:
        import aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048

        out["included_portal_product_arns"] = (
            aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048.deserialize_json(
                data["includedPortalProductArns"]
            )
        )
    if "lastModified" in data:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["last_modified"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.deserialize_json(
                data["lastModified"]
            )
        )
    if "lastPublished" in data:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["last_published"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.deserialize_json(
                data["lastPublished"]
            )
        )
    if "lastPublishedDescription" in data:
        out["last_published_description"] = data["lastPublishedDescription"]
    if "portalArn" in data:
        out["portal_arn"] = data["portalArn"]
    if "portalContent" in data:
        import aws_sdk_apigatewayv2.types.portal_content

        out["portal_content"] = (
            aws_sdk_apigatewayv2.types.portal_content.deserialize_json(
                data["portalContent"]
            )
        )
    if "portalId" in data:
        out["portal_id"] = data["portalId"]
    if "publishStatus" in data:
        import aws_sdk_apigatewayv2.types.publish_status

        out["publish_status"] = (
            aws_sdk_apigatewayv2.types.publish_status.deserialize_json(
                data["publishStatus"]
            )
        )
    if "rumAppMonitorName" in data:
        out["rum_app_monitor_name"] = data["rumAppMonitorName"]
    if "statusException" in data:
        import aws_sdk_apigatewayv2.types.status_exception

        out["status_exception"] = (
            aws_sdk_apigatewayv2.types.status_exception.deserialize_json(
                data["statusException"]
            )
        )
    if "tags" in data:
        import aws_sdk_apigatewayv2.types.tags

        out["tags"] = aws_sdk_apigatewayv2.types.tags.deserialize_json(data["tags"])
    return out
