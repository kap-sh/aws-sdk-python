"""Generated from Smithy shape ``com.amazonaws.sfn#TaskSubmittedEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.history_event_execution_data_details
    import capo_sfn.types.name
    import capo_sfn.types.sensitive_data


class TaskSubmittedEventDetails(TypedDict, closed=True):
    resource_type: "capo_sfn.types.name.Name"
    """<p>The service name of the resource in a task state.</p>"""
    resource: "capo_sfn.types.name.Name"
    """<p>The action of the resource called by a task state.</p>"""
    output: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The response from a resource when a task has started. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""
    output_details: NotRequired[
        "capo_sfn.types.history_event_execution_data_details.HistoryEventExecutionDataDetails"
    ]
    """<p>Contains details about the output of an execution history event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskSubmittedEventDetails) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    out["resource"] = value["resource"]
    if "output" in value:
        out["output"] = value["output"]
    if "output_details" in value:
        import capo_sfn.types.history_event_execution_data_details

        out["outputDetails"] = (
            capo_sfn.types.history_event_execution_data_details.serialize_aws_json_1_0(
                value["output_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TaskSubmittedEventDetails:
    out: TaskSubmittedEventDetails = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("TaskSubmittedEventDetails.resource_type required")
    if "resource" in data:
        out["resource"] = data["resource"]
    else:
        raise DeserializationError("TaskSubmittedEventDetails.resource required")
    if "output" in data:
        out["output"] = data["output"]
    if "outputDetails" in data:
        import capo_sfn.types.history_event_execution_data_details

        out["output_details"] = (
            capo_sfn.types.history_event_execution_data_details.deserialize_aws_json_1_0(
                data["outputDetails"]
            )
        )
    return out
