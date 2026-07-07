"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.endpoint_response


class DeleteEndpointResponse(TypedDict, closed=True):
    endpoint_response: NotRequired[
        "aws_sdk_pinpoint.types.endpoint_response.EndpointResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint_response" in value:
        import aws_sdk_pinpoint.types.endpoint_response

        out["EndpointResponse"] = (
            aws_sdk_pinpoint.types.endpoint_response.serialize_json(
                value["endpoint_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteEndpointResponse:
    out: DeleteEndpointResponse = {}  # type: ignore[typeddict-item]
    if "EndpointResponse" in data:
        import aws_sdk_pinpoint.types.endpoint_response

        out["endpoint_response"] = (
            aws_sdk_pinpoint.types.endpoint_response.deserialize_json(
                data["EndpointResponse"]
            )
        )
    return out
