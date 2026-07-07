"""Generated from Smithy shape ``com.amazonaws.sfn#StateEnteredEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.history_event_execution_data_details
    import aws_sdk_sfn.types.name
    import aws_sdk_sfn.types.sensitive_data


class StateEnteredEventDetails(TypedDict, closed=True):
    name: "aws_sdk_sfn.types.name.Name"
    """<p>The name of the state.</p>"""
    input: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The string that contains the JSON input data for the state. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""
    input_details: NotRequired[
        "aws_sdk_sfn.types.history_event_execution_data_details.HistoryEventExecutionDataDetails"
    ]
    """<p>Contains details about the input for an execution history event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateEnteredEventDetails) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "input" in value:
        out["input"] = value["input"]
    if "input_details" in value:
        import aws_sdk_sfn.types.history_event_execution_data_details

        out["inputDetails"] = (
            aws_sdk_sfn.types.history_event_execution_data_details.serialize_aws_json_1_0(
                value["input_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StateEnteredEventDetails:
    out: StateEnteredEventDetails = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StateEnteredEventDetails.name required")
    if "input" in data:
        out["input"] = data["input"]
    if "inputDetails" in data:
        import aws_sdk_sfn.types.history_event_execution_data_details

        out["input_details"] = (
            aws_sdk_sfn.types.history_event_execution_data_details.deserialize_aws_json_1_0(
                data["inputDetails"]
            )
        )
    return out
