"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FieldForReranking``."""

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError


class FieldForReranking(TypedDict, closed=True):
    field_name: "str"
    """<p>The name of the metadata field to include or exclude during reranking.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldForReranking) -> dict:
    out: dict = {}
    out["fieldName"] = value["field_name"]
    return out


def deserialize_json(data: dict) -> FieldForReranking:
    out: FieldForReranking = {}  # type: ignore[typeddict-item]
    if "fieldName" in data:
        out["field_name"] = data["fieldName"]
    else:
        raise DeserializationError("FieldForReranking.field_name required")
    return out
