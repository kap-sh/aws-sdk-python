"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DatasetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.dataset_arn
    import capo_lookoutequipment.types.dataset_name
    import capo_lookoutequipment.types.dataset_status
    import capo_lookoutequipment.types.timestamp


class DatasetSummary(TypedDict, closed=True):
    dataset_name: NotRequired["capo_lookoutequipment.types.dataset_name.DatasetName"]
    """<p>The name of the dataset. </p>"""
    dataset_arn: NotRequired["capo_lookoutequipment.types.dataset_arn.DatasetArn"]
    """<p>The Amazon Resource Name (ARN) of the specified dataset. </p>"""
    status: NotRequired["capo_lookoutequipment.types.dataset_status.DatasetStatus"]
    """<p>Indicates the status of the dataset. </p>"""
    created_at: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>The time at which the dataset was created in Amazon Lookout for Equipment. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatasetSummary) -> dict:
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
    if "created_at" in value:
        import capo_lookoutequipment.types.timestamp

        out["CreatedAt"] = capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DatasetSummary:
    out: DatasetSummary = {}  # type: ignore[typeddict-item]
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
    if "CreatedAt" in data:
        import capo_lookoutequipment.types.timestamp

        out["created_at"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    return out
