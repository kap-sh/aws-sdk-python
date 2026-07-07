"""Generated from Smithy shape ``com.amazonaws.sfn#TaskSucceededEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.history_event_execution_data_details
    import aws_sdk_sfn.types.name
    import aws_sdk_sfn.types.sensitive_data


class TaskSucceededEventDetails(TypedDict, closed=True):
    resource_type: "aws_sdk_sfn.types.name.Name"
    """<p>The service name of the resource in a task state.</p>"""
    resource: "aws_sdk_sfn.types.name.Name"
    """<p>The action of the resource called by a task state.</p>"""
    output: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The full JSON response from a resource when a task has succeeded. This response becomes the output of the related task. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""
    output_details: NotRequired[
        "aws_sdk_sfn.types.history_event_execution_data_details.HistoryEventExecutionDataDetails"
    ]
    """<p>Contains details about the output of an execution history event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskSucceededEventDetails) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    out["resource"] = value["resource"]
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


def deserialize_aws_json_1_0(data: dict) -> TaskSucceededEventDetails:
    out: TaskSucceededEventDetails = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("TaskSucceededEventDetails.resource_type required")
    if "resource" in data:
        out["resource"] = data["resource"]
    else:
        raise DeserializationError("TaskSucceededEventDetails.resource required")
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
