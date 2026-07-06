"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeleteCorsConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class DeleteCorsConfigurationRequest(TypedDict, closed=True):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCorsConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCorsConfigurationRequest:
    out: DeleteCorsConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
