"""Generated from Smithy shape ``com.amazonaws.iot#PutItemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.table_name


class PutItemInput(TypedDict, closed=True):
    table_name: "capo_iot.types.table_name.TableName"
    """<p>The table where the message data will be written.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutItemInput) -> dict:
    out: dict = {}
    out["tableName"] = value["table_name"]
    return out


def deserialize_json(data: dict) -> PutItemInput:
    out: PutItemInput = {}  # type: ignore[typeddict-item]
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    else:
        raise DeserializationError("PutItemInput.table_name required")
    return out
