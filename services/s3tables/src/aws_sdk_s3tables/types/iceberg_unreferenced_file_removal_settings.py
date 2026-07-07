"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergUnreferencedFileRemovalSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.positive_integer


class IcebergUnreferencedFileRemovalSettings(TypedDict, closed=True):
    unreferenced_days: NotRequired[
        "aws_sdk_s3tables.types.positive_integer.PositiveInteger"
    ]
    """<p>The number of days an object has to be unreferenced before it is marked as non-current.</p>"""
    non_current_days: NotRequired[
        "aws_sdk_s3tables.types.positive_integer.PositiveInteger"
    ]
    """<p>The number of days an object has to be non-current before it is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IcebergUnreferencedFileRemovalSettings) -> dict:
    out: dict = {}
    if "unreferenced_days" in value:
        out["unreferencedDays"] = value["unreferenced_days"]
    if "non_current_days" in value:
        out["nonCurrentDays"] = value["non_current_days"]
    return out


def deserialize_json(data: dict) -> IcebergUnreferencedFileRemovalSettings:
    out: IcebergUnreferencedFileRemovalSettings = {}  # type: ignore[typeddict-item]
    if "unreferencedDays" in data:
        out["unreferenced_days"] = data["unreferencedDays"]
    if "nonCurrentDays" in data:
        out["non_current_days"] = data["nonCurrentDays"]
    return out
