"""Generated from Smithy shape ``com.amazonaws.connecthealth#InsightsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connecthealth.types.s3_uri


class InsightsOutput(TypedDict, closed=True):
    uri: "capo_connecthealth.types.s3_uri.S3Uri"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightsOutput) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> InsightsOutput:
    out: InsightsOutput = {}  # type: ignore[typeddict-item]
    if "uri" in data:
        out["uri"] = data["uri"]
    else:
        raise DeserializationError("InsightsOutput.uri required")
    return out
