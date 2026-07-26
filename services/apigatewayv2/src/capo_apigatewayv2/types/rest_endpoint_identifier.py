"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#RestEndpointIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.identifier_parts


class RestEndpointIdentifier(TypedDict, closed=True):
    identifier_parts: NotRequired[
        "capo_apigatewayv2.types.identifier_parts.IdentifierParts"
    ]
    """<p>The identifier parts of the REST endpoint identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestEndpointIdentifier) -> dict:
    out: dict = {}
    if "identifier_parts" in value:
        import capo_apigatewayv2.types.identifier_parts

        out["identifierParts"] = (
            capo_apigatewayv2.types.identifier_parts.serialize_json(
                value["identifier_parts"]
            )
        )
    return out


def deserialize_json(data: dict) -> RestEndpointIdentifier:
    out: RestEndpointIdentifier = {}  # type: ignore[typeddict-item]
    if "identifierParts" in data:
        import capo_apigatewayv2.types.identifier_parts

        out["identifier_parts"] = (
            capo_apigatewayv2.types.identifier_parts.deserialize_json(
                data["identifierParts"]
            )
        )
    return out
