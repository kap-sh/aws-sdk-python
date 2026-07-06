"""Generated from Smithy shape ``com.amazonaws.databrew#JsonOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.multi_line


class JsonOptions(TypedDict, closed=True):
    multi_line: "aws_sdk_databrew.types.multi_line.MultiLine"
    """<p>A value that specifies whether JSON input contains embedded new line characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JsonOptions) -> dict:
    out: dict = {}
    out["MultiLine"] = value.get("multi_line", False)
    return out


def deserialize_json(data: dict) -> JsonOptions:
    out: JsonOptions = {}  # type: ignore[typeddict-item]
    if "MultiLine" in data:
        out["multi_line"] = data["MultiLine"]
    else:
        out["multi_line"] = False
    return out
