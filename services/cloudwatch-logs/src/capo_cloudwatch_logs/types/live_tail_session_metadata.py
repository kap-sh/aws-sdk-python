"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LiveTailSessionMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.is_sampled


class LiveTailSessionMetadata(TypedDict, closed=True):
    sampled: "capo_cloudwatch_logs.types.is_sampled.IsSampled"
    """<p>If this is <code>true</code>, then more than 500 log events matched the request for this update, and the <code>sessionResults</code> includes a sample of 500 of those events.</p> <p>If this is <code>false</code>, then 500 or fewer log events matched the request for this update, so no sampling was necessary. In this case, the <code>sessionResults</code> array includes all log events that matched your request during this time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LiveTailSessionMetadata) -> dict:
    out: dict = {}
    out["sampled"] = value.get("sampled", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> LiveTailSessionMetadata:
    out: LiveTailSessionMetadata = {}  # type: ignore[typeddict-item]
    if data.get("sampled") is not None:
        out["sampled"] = data["sampled"]
    else:
        out["sampled"] = False
    return out
