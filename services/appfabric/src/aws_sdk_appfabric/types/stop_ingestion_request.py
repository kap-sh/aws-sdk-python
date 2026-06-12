"""Generated from Smithy shape ``com.amazonaws.appfabric#StopIngestionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.identifier


class StopIngestionRequest(TypedDict):
    ingestion_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.</p>"""
    app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopIngestionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopIngestionRequest:
    out: StopIngestionRequest = {}  # type: ignore[typeddict-item]
    return out
