"""Generated from Smithy shape ``com.amazonaws.opensearch#GetApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.id


class GetApplicationRequest(TypedDict):
    id: "aws_sdk_opensearch.types.id.Id"
    """<p>The unique identifier of the OpenSearch application to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApplicationRequest:
    out: GetApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
