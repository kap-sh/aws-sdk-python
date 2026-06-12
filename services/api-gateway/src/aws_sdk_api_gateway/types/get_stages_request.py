"""Generated from Smithy shape ``com.amazonaws.apigateway#GetStagesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class GetStagesRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    deployment_id: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The stages' deployment identifiers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetStagesRequest:
    out: GetStagesRequest = {}  # type: ignore[typeddict-item]
    return out
