"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ReservationPlanSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer
    import aws_sdk_mediaconvert.types.commitment
    import aws_sdk_mediaconvert.types.renewal_type


class ReservationPlanSettings(TypedDict):
    commitment: NotRequired["aws_sdk_mediaconvert.types.commitment.Commitment"]
    """The length of the term of your reserved queue pricing plan commitment."""
    renewal_type: NotRequired["aws_sdk_mediaconvert.types.renewal_type.RenewalType"]
    """Specifies whether the term of your reserved queue pricing plan is automatically extended (AUTO_RENEW) or expires (EXPIRE) at the end of the term. When your term is auto renewed, you extend your commitment by 12 months from the auto renew date. You can cancel this commitment."""
    reserved_slots: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """Specifies the number of reserved transcode slots (RTS) for this queue. The number of RTS determines how many jobs the queue can process in parallel; each RTS can process one job at a time. You can't decrease the number of RTS in your reserved queue. You can increase the number of RTS by extending your existing commitment with a new 12-month commitment for the larger number. The new commitment begins when you purchase the additional capacity. You can't cancel your commitment or revert to your original commitment after you increase the capacity."""


# --- restJson1 ser/de ---
def serialize_json(value: ReservationPlanSettings) -> dict:
    out: dict = {}
    if "commitment" in value:
        import aws_sdk_mediaconvert.types.commitment

        out["commitment"] = aws_sdk_mediaconvert.types.commitment.serialize_json(
            value["commitment"]
        )
    if "renewal_type" in value:
        import aws_sdk_mediaconvert.types.renewal_type

        out["renewalType"] = aws_sdk_mediaconvert.types.renewal_type.serialize_json(
            value["renewal_type"]
        )
    if "reserved_slots" in value:
        out["reservedSlots"] = value["reserved_slots"]
    return out


def deserialize_json(data: dict) -> ReservationPlanSettings:
    out: ReservationPlanSettings = {}  # type: ignore[typeddict-item]
    if "commitment" in data:
        import aws_sdk_mediaconvert.types.commitment

        out["commitment"] = aws_sdk_mediaconvert.types.commitment.deserialize_json(
            data["commitment"]
        )
    if "renewalType" in data:
        import aws_sdk_mediaconvert.types.renewal_type

        out["renewal_type"] = aws_sdk_mediaconvert.types.renewal_type.deserialize_json(
            data["renewalType"]
        )
    if "reservedSlots" in data:
        out["reserved_slots"] = data["reservedSlots"]
    return out
