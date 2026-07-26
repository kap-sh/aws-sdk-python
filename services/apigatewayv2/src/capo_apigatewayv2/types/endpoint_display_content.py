"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#EndpointDisplayContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.display_content_overrides
    import capo_apigatewayv2.types.none


class EndpointDisplayContent(TypedDict, closed=True):
    none: NotRequired["capo_apigatewayv2.types.none.None_"]
    """<p>If your product REST endpoint contains no overrides, the none object is returned.</p>"""
    overrides: NotRequired[
        "capo_apigatewayv2.types.display_content_overrides.DisplayContentOverrides"
    ]
    """<p>The overrides for endpoint display content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointDisplayContent) -> dict:
    out: dict = {}
    if "none" in value:
        import capo_apigatewayv2.types.none

        out["none"] = capo_apigatewayv2.types.none.serialize_json(value["none"])
    if "overrides" in value:
        import capo_apigatewayv2.types.display_content_overrides

        out["overrides"] = (
            capo_apigatewayv2.types.display_content_overrides.serialize_json(
                value["overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> EndpointDisplayContent:
    out: EndpointDisplayContent = {}  # type: ignore[typeddict-item]
    if "none" in data:
        import capo_apigatewayv2.types.none

        out["none"] = capo_apigatewayv2.types.none.deserialize_json(data["none"])
    if "overrides" in data:
        import capo_apigatewayv2.types.display_content_overrides

        out["overrides"] = (
            capo_apigatewayv2.types.display_content_overrides.deserialize_json(
                data["overrides"]
            )
        )
    return out
