"""Generated from Smithy shape ``com.amazonaws.apigateway#GetSdkTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class GetSdkTypeRequest(TypedDict, closed=True):
    id: "aws_sdk_api_gateway.types.string.String"
    """<p>The identifier of the queried SdkType instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSdkTypeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSdkTypeRequest:
    out: GetSdkTypeRequest = {}  # type: ignore[typeddict-item]
    return out
