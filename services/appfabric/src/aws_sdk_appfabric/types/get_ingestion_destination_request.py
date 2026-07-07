"""Generated from Smithy shape ``com.amazonaws.appfabric#GetIngestionDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.identifier


class GetIngestionDestinationRequest(TypedDict, closed=True):
    app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""
    ingestion_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.</p>"""
    ingestion_destination_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion destination to use for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIngestionDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIngestionDestinationRequest:
    out: GetIngestionDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
