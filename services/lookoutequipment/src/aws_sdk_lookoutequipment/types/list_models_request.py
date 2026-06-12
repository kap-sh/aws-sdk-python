"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListModelsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.dataset_name
    import aws_sdk_lookoutequipment.types.max_results
    import aws_sdk_lookoutequipment.types.model_name
    import aws_sdk_lookoutequipment.types.model_status
    import aws_sdk_lookoutequipment.types.next_token


class ListModelsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_lookoutequipment.types.next_token.NextToken"]
    """<p> An opaque pagination token indicating where to continue the listing of machine learning models. </p>"""
    max_results: NotRequired["aws_sdk_lookoutequipment.types.max_results.MaxResults"]
    """<p> Specifies the maximum number of machine learning models to list. </p>"""
    status: NotRequired["aws_sdk_lookoutequipment.types.model_status.ModelStatus"]
    """<p>The status of the machine learning model. </p>"""
    model_name_begins_with: NotRequired[
        "aws_sdk_lookoutequipment.types.model_name.ModelName"
    ]
    """<p>The beginning of the name of the machine learning models being listed. </p>"""
    dataset_name_begins_with: NotRequired[
        "aws_sdk_lookoutequipment.types.dataset_name.DatasetName"
    ]
    """<p>The beginning of the name of the dataset of the machine learning models to be listed. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListModelsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "status" in value:
        import aws_sdk_lookoutequipment.types.model_status

        out["Status"] = (
            aws_sdk_lookoutequipment.types.model_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "model_name_begins_with" in value:
        out["ModelNameBeginsWith"] = value["model_name_begins_with"]
    if "dataset_name_begins_with" in value:
        out["DatasetNameBeginsWith"] = value["dataset_name_begins_with"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListModelsRequest:
    out: ListModelsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Status" in data:
        import aws_sdk_lookoutequipment.types.model_status

        out["status"] = (
            aws_sdk_lookoutequipment.types.model_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "ModelNameBeginsWith" in data:
        out["model_name_begins_with"] = data["ModelNameBeginsWith"]
    if "DatasetNameBeginsWith" in data:
        out["dataset_name_begins_with"] = data["DatasetNameBeginsWith"]
    return out
