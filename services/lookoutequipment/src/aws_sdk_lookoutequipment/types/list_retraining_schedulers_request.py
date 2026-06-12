"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListRetrainingSchedulersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.max_results
    import aws_sdk_lookoutequipment.types.model_name
    import aws_sdk_lookoutequipment.types.next_token
    import aws_sdk_lookoutequipment.types.retraining_scheduler_status


class ListRetrainingSchedulersRequest(TypedDict):
    model_name_begins_with: NotRequired[
        "aws_sdk_lookoutequipment.types.model_name.ModelName"
    ]
    """<p>Specify this field to only list retraining schedulers whose machine learning models begin with the value you specify. </p>"""
    status: NotRequired[
        "aws_sdk_lookoutequipment.types.retraining_scheduler_status.RetrainingSchedulerStatus"
    ]
    """<p>Specify this field to only list retraining schedulers whose status matches the value you specify. </p>"""
    next_token: NotRequired["aws_sdk_lookoutequipment.types.next_token.NextToken"]
    """<p>If the number of results exceeds the maximum, a pagination token is returned. Use the token in the request to show the next page of retraining schedulers.</p>"""
    max_results: NotRequired["aws_sdk_lookoutequipment.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of retraining schedulers to list. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRetrainingSchedulersRequest) -> dict:
    out: dict = {}
    if "model_name_begins_with" in value:
        out["ModelNameBeginsWith"] = value["model_name_begins_with"]
    if "status" in value:
        import aws_sdk_lookoutequipment.types.retraining_scheduler_status

        out["Status"] = (
            aws_sdk_lookoutequipment.types.retraining_scheduler_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRetrainingSchedulersRequest:
    out: ListRetrainingSchedulersRequest = {}  # type: ignore[typeddict-item]
    if "ModelNameBeginsWith" in data:
        out["model_name_begins_with"] = data["ModelNameBeginsWith"]
    if "Status" in data:
        import aws_sdk_lookoutequipment.types.retraining_scheduler_status

        out["status"] = (
            aws_sdk_lookoutequipment.types.retraining_scheduler_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
