"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeUpdateStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.data_lake_status
    import capo_securitylake.types.data_lake_update_exception


class DataLakeUpdateStatus(TypedDict, closed=True):
    request_id: NotRequired["str"]
    """<p>The unique ID for the last <code>UpdateDataLake</code> or <code>DeleteDataLake</code> API request.</p>"""
    status: NotRequired["capo_securitylake.types.data_lake_status.DataLakeStatus"]
    """<p>The status of the last <code>UpdateDataLake</code> or <code>DeleteDataLake</code> API request that was requested.</p>"""
    exception: NotRequired[
        "capo_securitylake.types.data_lake_update_exception.DataLakeUpdateException"
    ]
    """<p>The details of the last <code>UpdateDataLake</code>or <code>DeleteDataLake</code> API request which failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeUpdateStatus) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "status" in value:
        import capo_securitylake.types.data_lake_status

        out["status"] = capo_securitylake.types.data_lake_status.serialize_json(
            value["status"]
        )
    if "exception" in value:
        import capo_securitylake.types.data_lake_update_exception

        out["exception"] = (
            capo_securitylake.types.data_lake_update_exception.serialize_json(
                value["exception"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataLakeUpdateStatus:
    out: DataLakeUpdateStatus = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "status" in data:
        import capo_securitylake.types.data_lake_status

        out["status"] = capo_securitylake.types.data_lake_status.deserialize_json(
            data["status"]
        )
    if "exception" in data:
        import capo_securitylake.types.data_lake_update_exception

        out["exception"] = (
            capo_securitylake.types.data_lake_update_exception.deserialize_json(
                data["exception"]
            )
        )
    return out
