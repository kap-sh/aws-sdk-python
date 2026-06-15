"""Generated from Smithy shape ``com.amazonaws.lambda#WaitDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.execution_timestamp


class WaitDetails(TypedDict):
    scheduled_end_timestamp: NotRequired[
        "aws_sdk_lambda.types.execution_timestamp.ExecutionTimestamp"
    ]
    r"""<p>The date and time when the wait operation is scheduled to complete, in <a href=\"https://www.w3.org/TR/NOTE-datetime\">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaitDetails) -> dict:
    out: dict = {}
    if "scheduled_end_timestamp" in value:
        import aws_sdk_lambda.types.execution_timestamp

        out["ScheduledEndTimestamp"] = (
            aws_sdk_lambda.types.execution_timestamp.serialize_json(
                value["scheduled_end_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> WaitDetails:
    out: WaitDetails = {}  # type: ignore[typeddict-item]
    if "ScheduledEndTimestamp" in data:
        import aws_sdk_lambda.types.execution_timestamp

        out["scheduled_end_timestamp"] = (
            aws_sdk_lambda.types.execution_timestamp.deserialize_json(
                data["ScheduledEndTimestamp"]
            )
        )
    return out
