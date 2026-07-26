"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableRecordExpirationJobStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.table_arn


class GetTableRecordExpirationJobStatusRequest(TypedDict, closed=True):
    table_arn: "capo_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableRecordExpirationJobStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTableRecordExpirationJobStatusRequest:
    out: GetTableRecordExpirationJobStatusRequest = {}  # type: ignore[typeddict-item]
    return out
