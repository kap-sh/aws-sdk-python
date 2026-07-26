"""Generated from Smithy shape ``com.amazonaws.databrew#CsvOutputOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.delimiter


class CsvOutputOptions(TypedDict, closed=True):
    delimiter: NotRequired["capo_databrew.types.delimiter.Delimiter"]
    """<p>A single character that specifies the delimiter used to create CSV job output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CsvOutputOptions) -> dict:
    out: dict = {}
    if "delimiter" in value:
        out["Delimiter"] = value["delimiter"]
    return out


def deserialize_json(data: dict) -> CsvOutputOptions:
    out: CsvOutputOptions = {}  # type: ignore[typeddict-item]
    if "Delimiter" in data:
        out["delimiter"] = data["Delimiter"]
    return out
