"""Generated from Smithy shape ``com.amazonaws.dataexchange#AutoExportRevisionDestinationEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string


class AutoExportRevisionDestinationEntry(TypedDict):
    bucket: "aws_sdk_dataexchange.types.__string.__string"
    """<p>The Amazon S3 bucket that is the destination for the event action.</p>"""
    key_pattern: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>A string representing the pattern for generated names of the individual assets in the revision. For more information about key patterns, see <a href=\"https://docs.aws.amazon.com/data-exchange/latest/userguide/jobs.html#revision-export-keypatterns\">Key patterns when exporting revisions</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoExportRevisionDestinationEntry) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    if "key_pattern" in value:
        out["KeyPattern"] = value["key_pattern"]
    return out


def deserialize_json(data: dict) -> AutoExportRevisionDestinationEntry:
    out: AutoExportRevisionDestinationEntry = {}  # type: ignore[typeddict-item]
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    else:
        raise DeserializationError("AutoExportRevisionDestinationEntry.bucket required")
    if "KeyPattern" in data:
        out["key_pattern"] = data["KeyPattern"]
    return out
