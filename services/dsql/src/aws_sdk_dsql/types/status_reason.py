"""Generated from Smithy shape ``com.amazonaws.dsql#StatusReason``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dsql.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_dsql.types.stream_failure_error_code


class StatusReason(TypedDict):
    error: "aws_sdk_dsql.types.stream_failure_error_code.StreamFailureErrorCode"
    """<p>The error code for the stream failure.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the status was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatusReason) -> dict:
    out: dict = {}
    import aws_sdk_dsql.types.stream_failure_error_code

    out["error"] = aws_sdk_dsql.types.stream_failure_error_code.serialize_json(
        value["error"]
    )
    import aws_sdk_dsql.types._prelude.timestamp

    out["updatedAt"] = aws_sdk_dsql.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> StatusReason:
    out: StatusReason = {}  # type: ignore[typeddict-item]
    if "error" in data:
        import aws_sdk_dsql.types.stream_failure_error_code

        out["error"] = aws_sdk_dsql.types.stream_failure_error_code.deserialize_json(
            data["error"]
        )
    else:
        raise DeserializationError("StatusReason.error required")
    if "updatedAt" in data:
        import aws_sdk_dsql.types._prelude.timestamp

        out["updated_at"] = aws_sdk_dsql.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("StatusReason.updated_at required")
    return out
