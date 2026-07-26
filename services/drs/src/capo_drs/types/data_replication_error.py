"""Generated from Smithy shape ``com.amazonaws.drs#DataReplicationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.data_replication_error_string
    import capo_drs.types.large_bounded_string


class DataReplicationError(TypedDict, closed=True):
    error: NotRequired[
        "capo_drs.types.data_replication_error_string.DataReplicationErrorString"
    ]
    """<p>Error in data replication.</p>"""
    raw_error: NotRequired["capo_drs.types.large_bounded_string.LargeBoundedString"]
    """<p>Error in data replication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataReplicationError) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    if "raw_error" in value:
        out["rawError"] = value["raw_error"]
    return out


def deserialize_json(data: dict) -> DataReplicationError:
    out: DataReplicationError = {}  # type: ignore[typeddict-item]
    if "error" in data:
        out["error"] = data["error"]
    if "rawError" in data:
        out["raw_error"] = data["rawError"]
    return out
