"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ReservationPlan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer
    import capo_mediaconvert.types.__timestamp_unix
    import capo_mediaconvert.types.commitment
    import capo_mediaconvert.types.renewal_type
    import capo_mediaconvert.types.reservation_plan_status


class ReservationPlan(TypedDict, closed=True):
    commitment: NotRequired["capo_mediaconvert.types.commitment.Commitment"]
    """The length of the term of your reserved queue pricing plan commitment."""
    expires_at: NotRequired["capo_mediaconvert.types.__timestamp_unix.__timestampUnix"]
    """The timestamp in epoch seconds for when the current pricing plan term for this reserved queue expires."""
    purchased_at: NotRequired[
        "capo_mediaconvert.types.__timestamp_unix.__timestampUnix"
    ]
    """The timestamp in epoch seconds for when you set up the current pricing plan for this reserved queue."""
    renewal_type: NotRequired["capo_mediaconvert.types.renewal_type.RenewalType"]
    """Specifies whether the term of your reserved queue pricing plan is automatically extended (AUTO_RENEW) or expires (EXPIRE) at the end of the term."""
    reserved_slots: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """Specifies the number of reserved transcode slots (RTS) for this queue. The number of RTS determines how many jobs the queue can process in parallel; each RTS can process one job at a time. When you increase this number, you extend your existing commitment with a new 12-month commitment for a larger number of RTS. The new commitment begins when you purchase the additional capacity. You can't decrease the number of RTS in your reserved queue."""
    status: NotRequired[
        "capo_mediaconvert.types.reservation_plan_status.ReservationPlanStatus"
    ]
    """Specifies whether the pricing plan for your reserved queue is ACTIVE or EXPIRED."""


# --- restJson1 ser/de ---
def serialize_json(value: ReservationPlan) -> dict:
    out: dict = {}
    if "commitment" in value:
        import capo_mediaconvert.types.commitment

        out["commitment"] = capo_mediaconvert.types.commitment.serialize_json(
            value["commitment"]
        )
    if "expires_at" in value:
        import capo_mediaconvert.types.__timestamp_unix

        out["expiresAt"] = capo_mediaconvert.types.__timestamp_unix.serialize_json(
            value["expires_at"]
        )
    if "purchased_at" in value:
        import capo_mediaconvert.types.__timestamp_unix

        out["purchasedAt"] = capo_mediaconvert.types.__timestamp_unix.serialize_json(
            value["purchased_at"]
        )
    if "renewal_type" in value:
        import capo_mediaconvert.types.renewal_type

        out["renewalType"] = capo_mediaconvert.types.renewal_type.serialize_json(
            value["renewal_type"]
        )
    if "reserved_slots" in value:
        out["reservedSlots"] = value["reserved_slots"]
    if "status" in value:
        import capo_mediaconvert.types.reservation_plan_status

        out["status"] = capo_mediaconvert.types.reservation_plan_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> ReservationPlan:
    out: ReservationPlan = {}  # type: ignore[typeddict-item]
    if "commitment" in data:
        import capo_mediaconvert.types.commitment

        out["commitment"] = capo_mediaconvert.types.commitment.deserialize_json(
            data["commitment"]
        )
    if "expiresAt" in data:
        import capo_mediaconvert.types.__timestamp_unix

        out["expires_at"] = capo_mediaconvert.types.__timestamp_unix.deserialize_json(
            data["expiresAt"]
        )
    if "purchasedAt" in data:
        import capo_mediaconvert.types.__timestamp_unix

        out["purchased_at"] = capo_mediaconvert.types.__timestamp_unix.deserialize_json(
            data["purchasedAt"]
        )
    if "renewalType" in data:
        import capo_mediaconvert.types.renewal_type

        out["renewal_type"] = capo_mediaconvert.types.renewal_type.deserialize_json(
            data["renewalType"]
        )
    if "reservedSlots" in data:
        out["reserved_slots"] = data["reservedSlots"]
    if "status" in data:
        import capo_mediaconvert.types.reservation_plan_status

        out["status"] = (
            capo_mediaconvert.types.reservation_plan_status.deserialize_json(
                data["status"]
            )
        )
    return out
