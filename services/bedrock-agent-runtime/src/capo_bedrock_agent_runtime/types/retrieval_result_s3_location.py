"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultS3Location``."""

from typing_extensions import NotRequired, TypedDict


class RetrievalResultS3Location(TypedDict, closed=True):
    uri: NotRequired["str"]
    """<p>The S3 URI for the data source location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultS3Location) -> dict:
    out: dict = {}
    if "uri" in value:
        out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> RetrievalResultS3Location:
    out: RetrievalResultS3Location = {}  # type: ignore[typeddict-item]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    return out
