"""Generated from Smithy shape ``com.amazonaws.lakeformation#TransactionDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.timestamp
    import aws_sdk_lakeformation.types.transaction_id_string
    import aws_sdk_lakeformation.types.transaction_status


class TransactionDescription(TypedDict, closed=True):
    transaction_id: NotRequired[
        "aws_sdk_lakeformation.types.transaction_id_string.TransactionIdString"
    ]
    """<p>The ID of the transaction.</p>"""
    transaction_status: NotRequired[
        "aws_sdk_lakeformation.types.transaction_status.TransactionStatus"
    ]
    """<p>A status of ACTIVE, COMMITTED, or ABORTED.</p>"""
    transaction_start_time: NotRequired[
        "aws_sdk_lakeformation.types.timestamp.Timestamp"
    ]
    """<p>The time when the transaction started.</p>"""
    transaction_end_time: NotRequired["aws_sdk_lakeformation.types.timestamp.Timestamp"]
    """<p>The time when the transaction committed or aborted, if it is not currently active.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransactionDescription) -> dict:
    out: dict = {}
    if "transaction_id" in value:
        out["TransactionId"] = value["transaction_id"]
    if "transaction_status" in value:
        import aws_sdk_lakeformation.types.transaction_status

        out["TransactionStatus"] = (
            aws_sdk_lakeformation.types.transaction_status.serialize_json(
                value["transaction_status"]
            )
        )
    if "transaction_start_time" in value:
        import aws_sdk_lakeformation.types.timestamp

        out["TransactionStartTime"] = (
            aws_sdk_lakeformation.types.timestamp.serialize_json(
                value["transaction_start_time"]
            )
        )
    if "transaction_end_time" in value:
        import aws_sdk_lakeformation.types.timestamp

        out["TransactionEndTime"] = (
            aws_sdk_lakeformation.types.timestamp.serialize_json(
                value["transaction_end_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> TransactionDescription:
    out: TransactionDescription = {}  # type: ignore[typeddict-item]
    if "TransactionId" in data:
        out["transaction_id"] = data["TransactionId"]
    if "TransactionStatus" in data:
        import aws_sdk_lakeformation.types.transaction_status

        out["transaction_status"] = (
            aws_sdk_lakeformation.types.transaction_status.deserialize_json(
                data["TransactionStatus"]
            )
        )
    if "TransactionStartTime" in data:
        import aws_sdk_lakeformation.types.timestamp

        out["transaction_start_time"] = (
            aws_sdk_lakeformation.types.timestamp.deserialize_json(
                data["TransactionStartTime"]
            )
        )
    if "TransactionEndTime" in data:
        import aws_sdk_lakeformation.types.timestamp

        out["transaction_end_time"] = (
            aws_sdk_lakeformation.types.timestamp.deserialize_json(
                data["TransactionEndTime"]
            )
        )
    return out
