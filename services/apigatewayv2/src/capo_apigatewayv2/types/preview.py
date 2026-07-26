"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#Preview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string
    import capo_apigatewayv2.types.preview_status
    import capo_apigatewayv2.types.status_exception


class Preview(TypedDict, closed=True):
    preview_status: NotRequired["capo_apigatewayv2.types.preview_status.PreviewStatus"]
    """<p>The status of the preview.</p>"""
    preview_url: NotRequired["capo_apigatewayv2.types.__string.__string"]
    """<p>The URL of the preview.</p>"""
    status_exception: NotRequired[
        "capo_apigatewayv2.types.status_exception.StatusException"
    ]
    """<p>The status exception information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Preview) -> dict:
    out: dict = {}
    if "preview_status" in value:
        import capo_apigatewayv2.types.preview_status

        out["previewStatus"] = capo_apigatewayv2.types.preview_status.serialize_json(
            value["preview_status"]
        )
    if "preview_url" in value:
        out["previewUrl"] = value["preview_url"]
    if "status_exception" in value:
        import capo_apigatewayv2.types.status_exception

        out["statusException"] = (
            capo_apigatewayv2.types.status_exception.serialize_json(
                value["status_exception"]
            )
        )
    return out


def deserialize_json(data: dict) -> Preview:
    out: Preview = {}  # type: ignore[typeddict-item]
    if "previewStatus" in data:
        import capo_apigatewayv2.types.preview_status

        out["preview_status"] = capo_apigatewayv2.types.preview_status.deserialize_json(
            data["previewStatus"]
        )
    if "previewUrl" in data:
        out["preview_url"] = data["previewUrl"]
    if "statusException" in data:
        import capo_apigatewayv2.types.status_exception

        out["status_exception"] = (
            capo_apigatewayv2.types.status_exception.deserialize_json(
                data["statusException"]
            )
        )
    return out
