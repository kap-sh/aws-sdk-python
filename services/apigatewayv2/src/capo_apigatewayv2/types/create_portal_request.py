"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CreatePortalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__list_of__string_min20_max2048
    import capo_apigatewayv2.types.__string_min0_max255
    import capo_apigatewayv2.types.__string_min0_max1092
    import capo_apigatewayv2.types.authorization
    import capo_apigatewayv2.types.endpoint_configuration_request
    import capo_apigatewayv2.types.portal_content
    import capo_apigatewayv2.types.tags


class CreatePortalRequest(TypedDict, closed=True):
    authorization: NotRequired["capo_apigatewayv2.types.authorization.Authorization"]
    """<p>The authentication configuration for the portal.</p>"""
    endpoint_configuration: NotRequired[
        "capo_apigatewayv2.types.endpoint_configuration_request.EndpointConfigurationRequest"
    ]
    """<p>The domain configuration for the portal. Use a default domain provided by API Gateway or provide a fully-qualified domain name that you own.</p>"""
    included_portal_product_arns: NotRequired[
        "capo_apigatewayv2.types.__list_of__string_min20_max2048.__listOf__stringMin20Max2048"
    ]
    """<p>The ARNs of the portal products included in the portal.</p>"""
    logo_uri: NotRequired[
        "capo_apigatewayv2.types.__string_min0_max1092.__stringMin0Max1092"
    ]
    """<p>The URI for the portal logo image that is displayed in the portal header.</p>"""
    portal_content: NotRequired["capo_apigatewayv2.types.portal_content.PortalContent"]
    """<p>The content of the portal.</p>"""
    rum_app_monitor_name: NotRequired[
        "capo_apigatewayv2.types.__string_min0_max255.__stringMin0Max255"
    ]
    """<p>The name of the Amazon CloudWatch RUM app monitor for the portal.</p>"""
    tags: NotRequired["capo_apigatewayv2.types.tags.Tags"]
    """<p>The collection of tags. Each tag element is associated with a given resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePortalRequest) -> dict:
    out: dict = {}
    if "authorization" in value:
        import capo_apigatewayv2.types.authorization

        out["authorization"] = capo_apigatewayv2.types.authorization.serialize_json(
            value["authorization"]
        )
    if "endpoint_configuration" in value:
        import capo_apigatewayv2.types.endpoint_configuration_request

        out["endpointConfiguration"] = (
            capo_apigatewayv2.types.endpoint_configuration_request.serialize_json(
                value["endpoint_configuration"]
            )
        )
    if "included_portal_product_arns" in value:
        import capo_apigatewayv2.types.__list_of__string_min20_max2048

        out["includedPortalProductArns"] = (
            capo_apigatewayv2.types.__list_of__string_min20_max2048.serialize_json(
                value["included_portal_product_arns"]
            )
        )
    if "logo_uri" in value:
        out["logoUri"] = value["logo_uri"]
    if "portal_content" in value:
        import capo_apigatewayv2.types.portal_content

        out["portalContent"] = capo_apigatewayv2.types.portal_content.serialize_json(
            value["portal_content"]
        )
    if "rum_app_monitor_name" in value:
        out["rumAppMonitorName"] = value["rum_app_monitor_name"]
    if "tags" in value:
        import capo_apigatewayv2.types.tags

        out["tags"] = capo_apigatewayv2.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePortalRequest:
    out: CreatePortalRequest = {}  # type: ignore[typeddict-item]
    if "authorization" in data:
        import capo_apigatewayv2.types.authorization

        out["authorization"] = capo_apigatewayv2.types.authorization.deserialize_json(
            data["authorization"]
        )
    if "endpointConfiguration" in data:
        import capo_apigatewayv2.types.endpoint_configuration_request

        out["endpoint_configuration"] = (
            capo_apigatewayv2.types.endpoint_configuration_request.deserialize_json(
                data["endpointConfiguration"]
            )
        )
    if "includedPortalProductArns" in data:
        import capo_apigatewayv2.types.__list_of__string_min20_max2048

        out["included_portal_product_arns"] = (
            capo_apigatewayv2.types.__list_of__string_min20_max2048.deserialize_json(
                data["includedPortalProductArns"]
            )
        )
    if "logoUri" in data:
        out["logo_uri"] = data["logoUri"]
    if "portalContent" in data:
        import capo_apigatewayv2.types.portal_content

        out["portal_content"] = capo_apigatewayv2.types.portal_content.deserialize_json(
            data["portalContent"]
        )
    if "rumAppMonitorName" in data:
        out["rum_app_monitor_name"] = data["rumAppMonitorName"]
    if "tags" in data:
        import capo_apigatewayv2.types.tags

        out["tags"] = capo_apigatewayv2.types.tags.deserialize_json(data["tags"])
    return out
