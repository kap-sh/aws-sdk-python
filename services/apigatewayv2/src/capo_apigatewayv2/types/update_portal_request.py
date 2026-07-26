"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UpdatePortalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__list_of__string_min20_max2048
    import capo_apigatewayv2.types.__string
    import capo_apigatewayv2.types.__string_min0_max255
    import capo_apigatewayv2.types.__string_min0_max1092
    import capo_apigatewayv2.types.authorization
    import capo_apigatewayv2.types.endpoint_configuration_request
    import capo_apigatewayv2.types.portal_content


class UpdatePortalRequest(TypedDict, closed=True):
    authorization: NotRequired["capo_apigatewayv2.types.authorization.Authorization"]
    """<p>The authorization of the portal.</p>"""
    endpoint_configuration: NotRequired[
        "capo_apigatewayv2.types.endpoint_configuration_request.EndpointConfigurationRequest"
    ]
    """<p>Represents an endpoint configuration.</p>"""
    included_portal_product_arns: NotRequired[
        "capo_apigatewayv2.types.__list_of__string_min20_max2048.__listOf__stringMin20Max2048"
    ]
    """<p>The ARNs of the portal products included in the portal.</p>"""
    logo_uri: NotRequired[
        "capo_apigatewayv2.types.__string_min0_max1092.__stringMin0Max1092"
    ]
    """<p>The logo URI.</p>"""
    portal_content: NotRequired["capo_apigatewayv2.types.portal_content.PortalContent"]
    """<p>Contains the content that is visible to portal consumers including the themes, display names, and description.</p>"""
    portal_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The portal identifier.</p>"""
    rum_app_monitor_name: NotRequired[
        "capo_apigatewayv2.types.__string_min0_max255.__stringMin0Max255"
    ]
    """<p>The CloudWatch RUM app monitor name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePortalRequest) -> dict:
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
    return out


def deserialize_json(data: dict) -> UpdatePortalRequest:
    out: UpdatePortalRequest = {}  # type: ignore[typeddict-item]
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
    return out
