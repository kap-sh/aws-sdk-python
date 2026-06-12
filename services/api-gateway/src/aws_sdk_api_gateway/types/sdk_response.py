"""Generated from Smithy shape ``com.amazonaws.apigateway#SdkResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.blob
    import aws_sdk_api_gateway.types.string


class SdkResponse(TypedDict):
    content_type: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The content-type header value in the HTTP response.</p>"""
    content_disposition: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The content-disposition header value in the HTTP response.</p>"""
    body: NotRequired["aws_sdk_api_gateway.types.blob.Blob"]
    """<p>The binary blob response to GetSdk, which contains the generated SDK.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SdkResponse) -> dict:
    out: dict = {}
    if "body" in value:
        import aws_sdk_api_gateway.types.blob

        out["body"] = aws_sdk_api_gateway.types.blob.serialize_json(value["body"])
    return out


def deserialize_json(data: dict) -> SdkResponse:
    out: SdkResponse = {}  # type: ignore[typeddict-item]
    if "body" in data:
        import aws_sdk_api_gateway.types.blob

        out["body"] = aws_sdk_api_gateway.types.blob.deserialize_json(data["body"])
    return out
