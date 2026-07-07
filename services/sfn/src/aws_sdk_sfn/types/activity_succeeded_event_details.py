"""Generated from Smithy shape ``com.amazonaws.sfn#ActivitySucceededEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sfn.types.history_event_execution_data_details
    import aws_sdk_sfn.types.sensitive_data


class ActivitySucceededEventDetails(TypedDict, closed=True):
    output: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The JSON data output by the activity task. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""
    output_details: NotRequired[
        "aws_sdk_sfn.types.history_event_execution_data_details.HistoryEventExecutionDataDetails"
    ]
    """<p>Contains details about the output of an execution history event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivitySucceededEventDetails) -> dict:
    out: dict = {}
    if "output" in value:
        out["output"] = value["output"]
    if "output_details" in value:
        import aws_sdk_sfn.types.history_event_execution_data_details

        out["outputDetails"] = (
            aws_sdk_sfn.types.history_event_execution_data_details.serialize_aws_json_1_0(
                value["output_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivitySucceededEventDetails:
    out: ActivitySucceededEventDetails = {}  # type: ignore[typeddict-item]
    if "output" in data:
        out["output"] = data["output"]
    if "outputDetails" in data:
        import aws_sdk_sfn.types.history_event_execution_data_details

        out["output_details"] = (
            aws_sdk_sfn.types.history_event_execution_data_details.deserialize_aws_json_1_0(
                data["outputDetails"]
            )
        )
    return out
