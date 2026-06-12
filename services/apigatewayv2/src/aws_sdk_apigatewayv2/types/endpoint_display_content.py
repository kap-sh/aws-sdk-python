"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#EndpointDisplayContent``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.display_content_overrides
    import aws_sdk_apigatewayv2.types.none


class EndpointDisplayContent(TypedDict):
    none: NotRequired["aws_sdk_apigatewayv2.types.none.None"]
    """<p>If your product REST endpoint contains no overrides, the none object is returned.</p>"""
    overrides: NotRequired[
        "aws_sdk_apigatewayv2.types.display_content_overrides.DisplayContentOverrides"
    ]
    """<p>The overrides for endpoint display content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointDisplayContent) -> dict:
    out: dict = {}
    if "none" in value:
        import aws_sdk_apigatewayv2.types.none

        out["none"] = aws_sdk_apigatewayv2.types.none.serialize_json(value["none"])
    if "overrides" in value:
        import aws_sdk_apigatewayv2.types.display_content_overrides

        out["overrides"] = (
            aws_sdk_apigatewayv2.types.display_content_overrides.serialize_json(
                value["overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> EndpointDisplayContent:
    out: EndpointDisplayContent = {}  # type: ignore[typeddict-item]
    if "none" in data:
        import aws_sdk_apigatewayv2.types.none

        out["none"] = aws_sdk_apigatewayv2.types.none.deserialize_json(data["none"])
    if "overrides" in data:
        import aws_sdk_apigatewayv2.types.display_content_overrides

        out["overrides"] = (
            aws_sdk_apigatewayv2.types.display_content_overrides.deserialize_json(
                data["overrides"]
            )
        )
    return out
