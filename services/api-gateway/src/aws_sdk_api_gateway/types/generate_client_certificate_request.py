"""Generated from Smithy shape ``com.amazonaws.apigateway#GenerateClientCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.map_of_string_to_string
    import aws_sdk_api_gateway.types.string


class GenerateClientCertificateRequest(TypedDict, closed=True):
    description: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The description of the ClientCertificate.</p>"""
    tags: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateClientCertificateRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = aws_sdk_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GenerateClientCertificateRequest:
    out: GenerateClientCertificateRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["tags"]
            )
        )
    return out
