"""Generated from Smithy shape ``com.amazonaws.dsql#StatusReason``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dsql.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_dsql.types.stream_failure_error_code


class StatusReason(TypedDict, closed=True):
    error: "capo_dsql.types.stream_failure_error_code.StreamFailureErrorCode"
    """<p>The error code for the stream failure.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the status was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatusReason) -> dict:
    out: dict = {}
    import capo_dsql.types.stream_failure_error_code

    out["error"] = capo_dsql.types.stream_failure_error_code.serialize_json(
        value["error"]
    )
    import capo_dsql.types._prelude.timestamp

    out["updatedAt"] = capo_dsql.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> StatusReason:
    out: StatusReason = {}  # type: ignore[typeddict-item]
    if "error" in data:
        import capo_dsql.types.stream_failure_error_code

        out["error"] = capo_dsql.types.stream_failure_error_code.deserialize_json(
            data["error"]
        )
    else:
        raise DeserializationError("StatusReason.error required")
    if "updatedAt" in data:
        import capo_dsql.types._prelude.timestamp

        out["updated_at"] = capo_dsql.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("StatusReason.updated_at required")
    return out
