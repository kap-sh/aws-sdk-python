"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeleteApiRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class DeleteApiRequest(TypedDict):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApiRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteApiRequest:
    out: DeleteApiRequest = {}  # type: ignore[typeddict-item]
    return out
