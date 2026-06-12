"""Generated from Smithy shape ``com.amazonaws.apigateway#DeleteRestApiRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class DeleteRestApiRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRestApiRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRestApiRequest:
    out: DeleteRestApiRequest = {}  # type: ignore[typeddict-item]
    return out
