"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeUpdateException``."""

from typing import TypedDict

from typing_extensions import NotRequired


class DataLakeUpdateException(TypedDict):
    reason: NotRequired["str"]
    """<p>The reason for the exception of the last <code>UpdateDataLake</code>or <code>DeleteDataLake</code> API request.</p>"""
    code: NotRequired["str"]
    """<p>The reason code for the exception of the last <code>UpdateDataLake</code> or <code>DeleteDataLake</code> API request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeUpdateException) -> dict:
    out: dict = {}
    if "reason" in value:
        out["reason"] = value["reason"]
    if "code" in value:
        out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> DataLakeUpdateException:
    out: DataLakeUpdateException = {}  # type: ignore[typeddict-item]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "code" in data:
        out["code"] = data["code"]
    return out
