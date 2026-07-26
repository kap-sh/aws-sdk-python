"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CreateDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.dataset_arn
    import capo_lookoutequipment.types.dataset_name
    import capo_lookoutequipment.types.dataset_status


class CreateDatasetResponse(TypedDict, closed=True):
    dataset_name: NotRequired["capo_lookoutequipment.types.dataset_name.DatasetName"]
    """<p>The name of the dataset being created. </p>"""
    dataset_arn: NotRequired["capo_lookoutequipment.types.dataset_arn.DatasetArn"]
    """<p> The Amazon Resource Name (ARN) of the dataset being created. </p>"""
    status: NotRequired["capo_lookoutequipment.types.dataset_status.DatasetStatus"]
    """<p>Indicates the status of the <code>CreateDataset</code> operation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDatasetResponse) -> dict:
    out: dict = {}
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    if "status" in value:
        import capo_lookoutequipment.types.dataset_status

        out["Status"] = (
            capo_lookoutequipment.types.dataset_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDatasetResponse:
    out: CreateDatasetResponse = {}  # type: ignore[typeddict-item]
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    if "Status" in data:
        import capo_lookoutequipment.types.dataset_status

        out["status"] = (
            capo_lookoutequipment.types.dataset_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
