"""Generated from Smithy shape ``com.amazonaws.deadline#FixedBudgetSchedule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.ends_at
    import aws_sdk_deadline.types.starts_at


class FixedBudgetSchedule(TypedDict):
    start_time: "aws_sdk_deadline.types.starts_at.StartsAt"
    """<p>When the budget starts.</p>"""
    end_time: "aws_sdk_deadline.types.ends_at.EndsAt"
    """<p>When the budget ends.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FixedBudgetSchedule) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.starts_at

    out["startTime"] = aws_sdk_deadline.types.starts_at.serialize_json(
        value["start_time"]
    )
    import aws_sdk_deadline.types.ends_at

    out["endTime"] = aws_sdk_deadline.types.ends_at.serialize_json(value["end_time"])
    return out


def deserialize_json(data: dict) -> FixedBudgetSchedule:
    out: FixedBudgetSchedule = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_deadline.types.starts_at

        out["start_time"] = aws_sdk_deadline.types.starts_at.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("FixedBudgetSchedule.start_time required")
    if "endTime" in data:
        import aws_sdk_deadline.types.ends_at

        out["end_time"] = aws_sdk_deadline.types.ends_at.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError("FixedBudgetSchedule.end_time required")
    return out
