"""Generated from Smithy shape ``com.amazonaws.rdsdata#Record``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rds_data.types.row


class Record(TypedDict, closed=True):
    values: NotRequired["capo_rds_data.types.row.Row"]
    """<p>The values returned in the record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Record) -> dict:
    out: dict = {}
    if "values" in value:
        import capo_rds_data.types.row

        out["values"] = capo_rds_data.types.row.serialize_json(value["values"])
    return out


def deserialize_json(data: dict) -> Record:
    out: Record = {}  # type: ignore[typeddict-item]
    if "values" in data:
        import capo_rds_data.types.row

        out["values"] = capo_rds_data.types.row.deserialize_json(data["values"])
    return out
