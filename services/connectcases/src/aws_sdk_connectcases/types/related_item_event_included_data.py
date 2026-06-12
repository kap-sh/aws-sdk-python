"""Generated from Smithy shape ``com.amazonaws.connectcases#RelatedItemEventIncludedData``."""

from typing import TypedDict
from aws_sdk_connectcases.errors import DeserializationError


class RelatedItemEventIncludedData(TypedDict):
    include_content: "bool"
    """<p>Details of what related item data is published through the case event stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelatedItemEventIncludedData) -> dict:
    out: dict = {}
    out["includeContent"] = value["include_content"]
    return out


def deserialize_json(data: dict) -> RelatedItemEventIncludedData:
    out: RelatedItemEventIncludedData = {}  # type: ignore[typeddict-item]
    if "includeContent" in data:
        out["include_content"] = data["includeContent"]
    else:
        raise DeserializationError(
            "RelatedItemEventIncludedData.include_content required"
        )
    return out
