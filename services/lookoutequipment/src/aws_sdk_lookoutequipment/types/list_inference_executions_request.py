"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListInferenceExecutionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.inference_execution_status
    import aws_sdk_lookoutequipment.types.inference_scheduler_identifier
    import aws_sdk_lookoutequipment.types.max_results
    import aws_sdk_lookoutequipment.types.next_token
    import aws_sdk_lookoutequipment.types.timestamp


class ListInferenceExecutionsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_lookoutequipment.types.next_token.NextToken"]
    """<p>An opaque pagination token indicating where to continue the listing of inference executions.</p>"""
    max_results: NotRequired["aws_sdk_lookoutequipment.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of inference executions to list. </p>"""
    inference_scheduler_name: "aws_sdk_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier"
    """<p>The name of the inference scheduler for the inference execution listed. </p>"""
    data_start_time_after: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The time reference in the inferenced dataset after which Amazon Lookout for Equipment started the inference execution. </p>"""
    data_end_time_before: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The time reference in the inferenced dataset before which Amazon Lookout for Equipment stopped the inference execution. </p>"""
    status: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_execution_status.InferenceExecutionStatus"
    ]
    """<p>The status of the inference execution. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListInferenceExecutionsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    out["InferenceSchedulerName"] = value["inference_scheduler_name"]
    if "data_start_time_after" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["DataStartTimeAfter"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["data_start_time_after"]
            )
        )
    if "data_end_time_before" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["DataEndTimeBefore"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["data_end_time_before"]
            )
        )
    if "status" in value:
        import aws_sdk_lookoutequipment.types.inference_execution_status

        out["Status"] = (
            aws_sdk_lookoutequipment.types.inference_execution_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListInferenceExecutionsRequest:
    out: ListInferenceExecutionsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "InferenceSchedulerName" in data:
        out["inference_scheduler_name"] = data["InferenceSchedulerName"]
    else:
        raise DeserializationError(
            "ListInferenceExecutionsRequest.inference_scheduler_name required"
        )
    if "DataStartTimeAfter" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["data_start_time_after"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["DataStartTimeAfter"]
            )
        )
    if "DataEndTimeBefore" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["data_end_time_before"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["DataEndTimeBefore"]
            )
        )
    if "Status" in data:
        import aws_sdk_lookoutequipment.types.inference_execution_status

        out["status"] = (
            aws_sdk_lookoutequipment.types.inference_execution_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
