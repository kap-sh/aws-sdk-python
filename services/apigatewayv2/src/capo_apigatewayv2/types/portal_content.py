"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#PortalContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string_min0_max1024
    import capo_apigatewayv2.types.__string_min3_max255
    import capo_apigatewayv2.types.portal_theme


class PortalContent(TypedDict, closed=True):
    description: NotRequired[
        "capo_apigatewayv2.types.__string_min0_max1024.__stringMin0Max1024"
    ]
    """<p>A description of the portal.</p>"""
    display_name: NotRequired[
        "capo_apigatewayv2.types.__string_min3_max255.__stringMin3Max255"
    ]
    """<p>The display name for the portal.</p>"""
    theme: NotRequired["capo_apigatewayv2.types.portal_theme.PortalTheme"]
    """<p>The theme for the portal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortalContent) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "theme" in value:
        import capo_apigatewayv2.types.portal_theme

        out["theme"] = capo_apigatewayv2.types.portal_theme.serialize_json(
            value["theme"]
        )
    return out


def deserialize_json(data: dict) -> PortalContent:
    out: PortalContent = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "theme" in data:
        import capo_apigatewayv2.types.portal_theme

        out["theme"] = capo_apigatewayv2.types.portal_theme.deserialize_json(
            data["theme"]
        )
    return out
