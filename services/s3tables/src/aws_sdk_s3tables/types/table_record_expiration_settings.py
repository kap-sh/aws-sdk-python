"""Generated from Smithy shape ``com.amazonaws.s3tables#TableRecordExpirationSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.positive_integer


class TableRecordExpirationSettings(TypedDict):
    days: NotRequired["aws_sdk_s3tables.types.positive_integer.PositiveInteger"]
    """<p>If you enable record expiration for a table, you can specify the number of days to retain your table records. For example, to retain your table records for one year, set this value to <code>365</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableRecordExpirationSettings) -> dict:
    out: dict = {}
    if "days" in value:
        out["days"] = value["days"]
    return out


def deserialize_json(data: dict) -> TableRecordExpirationSettings:
    out: TableRecordExpirationSettings = {}  # type: ignore[typeddict-item]
    if "days" in data:
        out["days"] = data["days"]
    return out
