"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeDatasetGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.dataset_group


class DescribeDatasetGroupResponse(TypedDict):
    dataset_group: NotRequired["aws_sdk_personalize.types.dataset_group.DatasetGroup"]
    """<p>A listing of the dataset group's properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetGroupResponse) -> dict:
    out: dict = {}
    if "dataset_group" in value:
        import aws_sdk_personalize.types.dataset_group

        out["datasetGroup"] = (
            aws_sdk_personalize.types.dataset_group.serialize_aws_json_1_1(
                value["dataset_group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetGroupResponse:
    out: DescribeDatasetGroupResponse = {}  # type: ignore[typeddict-item]
    if "datasetGroup" in data:
        import aws_sdk_personalize.types.dataset_group

        out["dataset_group"] = (
            aws_sdk_personalize.types.dataset_group.deserialize_aws_json_1_1(
                data["datasetGroup"]
            )
        )
    return out
