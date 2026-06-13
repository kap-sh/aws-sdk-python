"""Generated from Smithy shape ``com.amazonaws.rum#DataStorage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rum.types.cw_log


class DataStorage(TypedDict):
    cw_log: NotRequired["aws_sdk_rum.types.cw_log.CwLog"]
    """<p>A structure that contains the information about whether the app monitor stores copies of the data that RUM collects in CloudWatch Logs. If it does, this structure also contains the name of the log group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataStorage) -> dict:
    out: dict = {}
    if "cw_log" in value:
        import aws_sdk_rum.types.cw_log

        out["CwLog"] = aws_sdk_rum.types.cw_log.serialize_json(value["cw_log"])
    return out


def deserialize_json(data: dict) -> DataStorage:
    out: DataStorage = {}  # type: ignore[typeddict-item]
    if "CwLog" in data:
        import aws_sdk_rum.types.cw_log

        out["cw_log"] = aws_sdk_rum.types.cw_log.deserialize_json(data["CwLog"])
    return out
