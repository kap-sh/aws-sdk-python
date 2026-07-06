"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetUserEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.endpoints_response


class GetUserEndpointsResponse(TypedDict, closed=True):
    endpoints_response: NotRequired[
        "aws_sdk_pinpoint.types.endpoints_response.EndpointsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetUserEndpointsResponse) -> dict:
    out: dict = {}
    if "endpoints_response" in value:
        import aws_sdk_pinpoint.types.endpoints_response

        out["EndpointsResponse"] = (
            aws_sdk_pinpoint.types.endpoints_response.serialize_json(
                value["endpoints_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetUserEndpointsResponse:
    out: GetUserEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "EndpointsResponse" in data:
        import aws_sdk_pinpoint.types.endpoints_response

        out["endpoints_response"] = (
            aws_sdk_pinpoint.types.endpoints_response.deserialize_json(
                data["EndpointsResponse"]
            )
        )
    return out
