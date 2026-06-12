"""Generated from Smithy shape ``com.amazonaws.appfabric#DeleteIngestionDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.identifier


class DeleteIngestionDestinationRequest(TypedDict):
    app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""
    ingestion_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.</p>"""
    ingestion_destination_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion destination to use for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIngestionDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIngestionDestinationRequest:
    out: DeleteIngestionDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
