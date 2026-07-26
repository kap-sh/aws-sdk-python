"""Generated from Smithy shape ``com.amazonaws.rum#DataStorage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rum.types.cw_log


class DataStorage(TypedDict, closed=True):
    cw_log: NotRequired["capo_rum.types.cw_log.CwLog"]
    """<p>A structure that contains the information about whether the app monitor stores copies of the data that RUM collects in CloudWatch Logs. If it does, this structure also contains the name of the log group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataStorage) -> dict:
    out: dict = {}
    if "cw_log" in value:
        import capo_rum.types.cw_log

        out["CwLog"] = capo_rum.types.cw_log.serialize_json(value["cw_log"])
    return out


def deserialize_json(data: dict) -> DataStorage:
    out: DataStorage = {}  # type: ignore[typeddict-item]
    if "CwLog" in data:
        import capo_rum.types.cw_log

        out["cw_log"] = capo_rum.types.cw_log.deserialize_json(data["CwLog"])
    return out
