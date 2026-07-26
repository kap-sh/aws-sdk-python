"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteUserEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.endpoints_response


class DeleteUserEndpointsResponse(TypedDict, closed=True):
    endpoints_response: NotRequired[
        "capo_pinpoint.types.endpoints_response.EndpointsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUserEndpointsResponse) -> dict:
    out: dict = {}
    if "endpoints_response" in value:
        import capo_pinpoint.types.endpoints_response

        out["EndpointsResponse"] = (
            capo_pinpoint.types.endpoints_response.serialize_json(
                value["endpoints_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteUserEndpointsResponse:
    out: DeleteUserEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "EndpointsResponse" in data:
        import capo_pinpoint.types.endpoints_response

        out["endpoints_response"] = (
            capo_pinpoint.types.endpoints_response.deserialize_json(
                data["EndpointsResponse"]
            )
        )
    return out
