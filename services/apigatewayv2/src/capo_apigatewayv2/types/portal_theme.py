"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#PortalTheme``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__timestamp_iso8601
    import capo_apigatewayv2.types.custom_colors


class PortalTheme(TypedDict, closed=True):
    custom_colors: NotRequired["capo_apigatewayv2.types.custom_colors.CustomColors"]
    """<p>Defines custom color values.</p>"""
    logo_last_uploaded: NotRequired[
        "capo_apigatewayv2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The timestamp when the logo was last uploaded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortalTheme) -> dict:
    out: dict = {}
    if "custom_colors" in value:
        import capo_apigatewayv2.types.custom_colors

        out["customColors"] = capo_apigatewayv2.types.custom_colors.serialize_json(
            value["custom_colors"]
        )
    if "logo_last_uploaded" in value:
        import capo_apigatewayv2.types.__timestamp_iso8601

        out["logoLastUploaded"] = (
            capo_apigatewayv2.types.__timestamp_iso8601.serialize_json(
                value["logo_last_uploaded"]
            )
        )
    return out


def deserialize_json(data: dict) -> PortalTheme:
    out: PortalTheme = {}  # type: ignore[typeddict-item]
    if "customColors" in data:
        import capo_apigatewayv2.types.custom_colors

        out["custom_colors"] = capo_apigatewayv2.types.custom_colors.deserialize_json(
            data["customColors"]
        )
    if "logoLastUploaded" in data:
        import capo_apigatewayv2.types.__timestamp_iso8601

        out["logo_last_uploaded"] = (
            capo_apigatewayv2.types.__timestamp_iso8601.deserialize_json(
                data["logoLastUploaded"]
            )
        )
    return out
