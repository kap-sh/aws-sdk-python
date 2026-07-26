"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateEndpointsBatchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.endpoint_batch_request


class UpdateEndpointsBatchRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    endpoint_batch_request: NotRequired[
        "capo_pinpoint.types.endpoint_batch_request.EndpointBatchRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEndpointsBatchRequest) -> dict:
    out: dict = {}
    if "endpoint_batch_request" in value:
        import capo_pinpoint.types.endpoint_batch_request

        out["EndpointBatchRequest"] = (
            capo_pinpoint.types.endpoint_batch_request.serialize_json(
                value["endpoint_batch_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateEndpointsBatchRequest:
    out: UpdateEndpointsBatchRequest = {}  # type: ignore[typeddict-item]
    if "EndpointBatchRequest" in data:
        import capo_pinpoint.types.endpoint_batch_request

        out["endpoint_batch_request"] = (
            capo_pinpoint.types.endpoint_batch_request.deserialize_json(
                data["EndpointBatchRequest"]
            )
        )
    return out
