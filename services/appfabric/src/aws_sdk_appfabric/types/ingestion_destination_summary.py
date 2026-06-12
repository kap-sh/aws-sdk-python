"""Generated from Smithy shape ``com.amazonaws.appfabric#IngestionDestinationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.arn


class IngestionDestinationSummary(TypedDict):
    arn: "aws_sdk_appfabric.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the ingestion destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestionDestinationSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> IngestionDestinationSummary:
    out: IngestionDestinationSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IngestionDestinationSummary.arn required")
    return out
