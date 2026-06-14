"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#RestEndpointIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.identifier_parts


class RestEndpointIdentifier(TypedDict):
    identifier_parts: NotRequired[
        "aws_sdk_apigatewayv2.types.identifier_parts.IdentifierParts"
    ]
    """<p>The identifier parts of the REST endpoint identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestEndpointIdentifier) -> dict:
    out: dict = {}
    if "identifier_parts" in value:
        import aws_sdk_apigatewayv2.types.identifier_parts

        out["identifierParts"] = (
            aws_sdk_apigatewayv2.types.identifier_parts.serialize_json(
                value["identifier_parts"]
            )
        )
    return out


def deserialize_json(data: dict) -> RestEndpointIdentifier:
    out: RestEndpointIdentifier = {}  # type: ignore[typeddict-item]
    if "identifierParts" in data:
        import aws_sdk_apigatewayv2.types.identifier_parts

        out["identifier_parts"] = (
            aws_sdk_apigatewayv2.types.identifier_parts.deserialize_json(
                data["identifierParts"]
            )
        )
    return out
