"""Generated from Smithy shape ``com.amazonaws.neptunedata#PropertygraphData``."""

from typing_extensions import NotRequired, TypedDict

from capo_neptunedata.errors import DeserializationError

PropertygraphData = TypedDict(
    "PropertygraphData",
    {
        "id": "str",
        "type": "str",
        "key": "str",
        "value": "object",
        "from": NotRequired["str"],
        "to": NotRequired["str"],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: PropertygraphData) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["type"] = value["type"]
    out["key"] = value["key"]
    out["value"] = value["value"]
    if "from" in value:
        out["from"] = value["from"]
    if "to" in value:
        out["to"] = value["to"]
    return out


def deserialize_json(data: dict) -> PropertygraphData:
    out: PropertygraphData = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("PropertygraphData.id required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("PropertygraphData.type required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("PropertygraphData.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("PropertygraphData.value required")
    if "from" in data:
        out["from"] = data["from"]
    if "to" in data:
        out["to"] = data["to"]
    return out
