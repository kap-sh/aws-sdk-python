"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_arc_zonal_shift.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.conflict_exception_reason


class ConflictException_(TypedDict, closed=True):
    message: "str"
    reason: (
        "capo_arc_zonal_shift.types.conflict_exception_reason.ConflictExceptionReason"
    )
    """<p>The reason for the conflict exception.</p>"""
    zonal_shift_id: NotRequired["str"]
    """<p>The zonal shift ID associated with the conflict exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_arc_zonal_shift.types.conflict_exception_reason

    out["reason"] = capo_arc_zonal_shift.types.conflict_exception_reason.serialize_json(
        value["reason"]
    )
    if "zonal_shift_id" in value:
        out["zonalShiftId"] = value["zonal_shift_id"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if "reason" in data:
        import capo_arc_zonal_shift.types.conflict_exception_reason

        out["reason"] = (
            capo_arc_zonal_shift.types.conflict_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    else:
        raise DeserializationError("ConflictException_.reason required")
    if "zonalShiftId" in data:
        out["zonal_shift_id"] = data["zonalShiftId"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.arczonalshift#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConflictException":
        return cls(deserialize_json(data))
