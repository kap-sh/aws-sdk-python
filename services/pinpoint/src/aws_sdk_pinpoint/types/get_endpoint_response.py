"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.endpoint_response


class GetEndpointResponse(TypedDict):
    endpoint_response: NotRequired[
        "aws_sdk_pinpoint.types.endpoint_response.EndpointResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint_response" in value:
        import aws_sdk_pinpoint.types.endpoint_response

        out["EndpointResponse"] = (
            aws_sdk_pinpoint.types.endpoint_response.serialize_json(
                value["endpoint_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetEndpointResponse:
    out: GetEndpointResponse = {}  # type: ignore[typeddict-item]
    if "EndpointResponse" in data:
        import aws_sdk_pinpoint.types.endpoint_response

        out["endpoint_response"] = (
            aws_sdk_pinpoint.types.endpoint_response.deserialize_json(
                data["EndpointResponse"]
            )
        )
    return out
