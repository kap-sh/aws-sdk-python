"""Generated from Smithy shape ``com.amazonaws.connect#AfterContactWorkConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.after_contact_work_time_limit


class AfterContactWorkConfig(TypedDict, closed=True):
    after_contact_work_time_limit: (
        "aws_sdk_connect.types.after_contact_work_time_limit.AfterContactWorkTimeLimit"
    )
    """<p>The ACW timeout duration in seconds. Minimum: 1 second. Maximum: 2,000,000 seconds (24 days). Enter 0 for indefinite ACW time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AfterContactWorkConfig) -> dict:
    out: dict = {}
    out["AfterContactWorkTimeLimit"] = value.get("after_contact_work_time_limit", 0)
    return out


def deserialize_json(data: dict) -> AfterContactWorkConfig:
    out: AfterContactWorkConfig = {}  # type: ignore[typeddict-item]
    if "AfterContactWorkTimeLimit" in data:
        out["after_contact_work_time_limit"] = data["AfterContactWorkTimeLimit"]
    else:
        out["after_contact_work_time_limit"] = 0
    return out
