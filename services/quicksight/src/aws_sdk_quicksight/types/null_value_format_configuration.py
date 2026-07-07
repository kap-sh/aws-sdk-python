"""Generated from Smithy shape ``com.amazonaws.quicksight#NullValueFormatConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.null_string


class NullValueFormatConfiguration(TypedDict, closed=True):
    null_string: "aws_sdk_quicksight.types.null_string.NullString"
    """<p>Determines the null string of null values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NullValueFormatConfiguration) -> dict:
    out: dict = {}
    out["NullString"] = value["null_string"]
    return out


def deserialize_json(data: dict) -> NullValueFormatConfiguration:
    out: NullValueFormatConfiguration = {}  # type: ignore[typeddict-item]
    if "NullString" in data:
        out["null_string"] = data["NullString"]
    else:
        raise DeserializationError("NullValueFormatConfiguration.null_string required")
    return out
