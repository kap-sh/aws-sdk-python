"""Generated from Smithy shape ``com.amazonaws.qconnect#QueryTextInputData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.query_text


class QueryTextInputData(TypedDict, closed=True):
    text: "aws_sdk_qconnect.types.query_text.QueryText"
    """<p>The text to search for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryTextInputData) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> QueryTextInputData:
    out: QueryTextInputData = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    else:
        raise DeserializationError("QueryTextInputData.text required")
    return out
