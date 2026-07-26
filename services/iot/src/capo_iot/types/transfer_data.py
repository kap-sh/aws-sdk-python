"""Generated from Smithy shape ``com.amazonaws.iot#TransferData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.date_type
    import capo_iot.types.message


class TransferData(TypedDict, closed=True):
    transfer_message: NotRequired["capo_iot.types.message.Message"]
    """<p>The transfer message.</p>"""
    reject_reason: NotRequired["capo_iot.types.message.Message"]
    """<p>The reason why the transfer was rejected.</p>"""
    transfer_date: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The date the transfer took place.</p>"""
    accept_date: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The date the transfer was accepted.</p>"""
    reject_date: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The date the transfer was rejected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransferData) -> dict:
    out: dict = {}
    if "transfer_message" in value:
        out["transferMessage"] = value["transfer_message"]
    if "reject_reason" in value:
        out["rejectReason"] = value["reject_reason"]
    if "transfer_date" in value:
        import capo_iot.types.date_type

        out["transferDate"] = capo_iot.types.date_type.serialize_json(
            value["transfer_date"]
        )
    if "accept_date" in value:
        import capo_iot.types.date_type

        out["acceptDate"] = capo_iot.types.date_type.serialize_json(
            value["accept_date"]
        )
    if "reject_date" in value:
        import capo_iot.types.date_type

        out["rejectDate"] = capo_iot.types.date_type.serialize_json(
            value["reject_date"]
        )
    return out


def deserialize_json(data: dict) -> TransferData:
    out: TransferData = {}  # type: ignore[typeddict-item]
    if "transferMessage" in data:
        out["transfer_message"] = data["transferMessage"]
    if "rejectReason" in data:
        out["reject_reason"] = data["rejectReason"]
    if "transferDate" in data:
        import capo_iot.types.date_type

        out["transfer_date"] = capo_iot.types.date_type.deserialize_json(
            data["transferDate"]
        )
    if "acceptDate" in data:
        import capo_iot.types.date_type

        out["accept_date"] = capo_iot.types.date_type.deserialize_json(
            data["acceptDate"]
        )
    if "rejectDate" in data:
        import capo_iot.types.date_type

        out["reject_date"] = capo_iot.types.date_type.deserialize_json(
            data["rejectDate"]
        )
    return out
