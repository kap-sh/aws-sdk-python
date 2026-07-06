"""Generated from Smithy shape ``com.amazonaws.appfabric#GetIngestionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.identifier


class GetIngestionRequest(TypedDict, closed=True):
    app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""
    ingestion_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIngestionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIngestionRequest:
    out: GetIngestionRequest = {}  # type: ignore[typeddict-item]
    return out
