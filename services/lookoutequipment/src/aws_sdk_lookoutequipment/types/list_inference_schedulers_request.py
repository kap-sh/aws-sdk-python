"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListInferenceSchedulersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.inference_scheduler_identifier
    import aws_sdk_lookoutequipment.types.inference_scheduler_status
    import aws_sdk_lookoutequipment.types.max_results
    import aws_sdk_lookoutequipment.types.model_name
    import aws_sdk_lookoutequipment.types.next_token


class ListInferenceSchedulersRequest(TypedDict):
    next_token: NotRequired["aws_sdk_lookoutequipment.types.next_token.NextToken"]
    """<p> An opaque pagination token indicating where to continue the listing of inference schedulers. </p>"""
    max_results: NotRequired["aws_sdk_lookoutequipment.types.max_results.MaxResults"]
    """<p> Specifies the maximum number of inference schedulers to list. </p>"""
    inference_scheduler_name_begins_with: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier"
    ]
    """<p>The beginning of the name of the inference schedulers to be listed. </p>"""
    model_name: NotRequired["aws_sdk_lookoutequipment.types.model_name.ModelName"]
    """<p>The name of the machine learning model used by the inference scheduler to be listed. </p>"""
    status: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_scheduler_status.InferenceSchedulerStatus"
    ]
    """<p>Specifies the current status of the inference schedulers.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListInferenceSchedulersRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "inference_scheduler_name_begins_with" in value:
        out["InferenceSchedulerNameBeginsWith"] = value[
            "inference_scheduler_name_begins_with"
        ]
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "status" in value:
        import aws_sdk_lookoutequipment.types.inference_scheduler_status

        out["Status"] = (
            aws_sdk_lookoutequipment.types.inference_scheduler_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListInferenceSchedulersRequest:
    out: ListInferenceSchedulersRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "InferenceSchedulerNameBeginsWith" in data:
        out["inference_scheduler_name_begins_with"] = data[
            "InferenceSchedulerNameBeginsWith"
        ]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "Status" in data:
        import aws_sdk_lookoutequipment.types.inference_scheduler_status

        out["status"] = (
            aws_sdk_lookoutequipment.types.inference_scheduler_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
