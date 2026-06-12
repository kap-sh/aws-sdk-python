"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteUserEndpointsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.endpoints_response


class DeleteUserEndpointsResponse(TypedDict):
    endpoints_response: NotRequired[
        "aws_sdk_pinpoint.types.endpoints_response.EndpointsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUserEndpointsResponse) -> dict:
    out: dict = {}
    if "endpoints_response" in value:
        import aws_sdk_pinpoint.types.endpoints_response

        out["EndpointsResponse"] = (
            aws_sdk_pinpoint.types.endpoints_response.serialize_json(
                value["endpoints_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteUserEndpointsResponse:
    out: DeleteUserEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "EndpointsResponse" in data:
        import aws_sdk_pinpoint.types.endpoints_response

        out["endpoints_response"] = (
            aws_sdk_pinpoint.types.endpoints_response.deserialize_json(
                data["EndpointsResponse"]
            )
        )
    return out
