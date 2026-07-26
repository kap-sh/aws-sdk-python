"""Generated from Smithy shape ``com.amazonaws.glacier#InputSerialization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.csv_input


class InputSerialization(TypedDict, closed=True):
    csv: NotRequired["capo_glacier.types.csv_input.CSVInput"]
    """<p>Describes the serialization of a CSV-encoded object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputSerialization) -> dict:
    out: dict = {}
    if "csv" in value:
        import capo_glacier.types.csv_input

        out["csv"] = capo_glacier.types.csv_input.serialize_json(value["csv"])
    return out


def deserialize_json(data: dict) -> InputSerialization:
    out: InputSerialization = {}  # type: ignore[typeddict-item]
    if "csv" in data:
        import capo_glacier.types.csv_input

        out["csv"] = capo_glacier.types.csv_input.deserialize_json(data["csv"])
    return out
