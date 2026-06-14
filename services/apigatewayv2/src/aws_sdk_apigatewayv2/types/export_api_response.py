"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ExportApiResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.exported_api


class ExportApiResponse(TypedDict):
    body: NotRequired["aws_sdk_apigatewayv2.types.exported_api.ExportedApi"]


# --- restJson1 ser/de ---
def serialize_json(value: ExportApiResponse) -> dict:
    out: dict = {}
    if "body" in value:
        import aws_sdk_apigatewayv2.types.exported_api

        out["body"] = aws_sdk_apigatewayv2.types.exported_api.serialize_json(
            value["body"]
        )
    return out


def deserialize_json(data: dict) -> ExportApiResponse:
    out: ExportApiResponse = {}  # type: ignore[typeddict-item]
    if "body" in data:
        import aws_sdk_apigatewayv2.types.exported_api

        out["body"] = aws_sdk_apigatewayv2.types.exported_api.deserialize_json(
            data["body"]
        )
    return out
