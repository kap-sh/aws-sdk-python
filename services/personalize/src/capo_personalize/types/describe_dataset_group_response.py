"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeDatasetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.dataset_group


class DescribeDatasetGroupResponse(TypedDict, closed=True):
    dataset_group: NotRequired["capo_personalize.types.dataset_group.DatasetGroup"]
    """<p>A listing of the dataset group's properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetGroupResponse) -> dict:
    out: dict = {}
    if "dataset_group" in value:
        import capo_personalize.types.dataset_group

        out["datasetGroup"] = (
            capo_personalize.types.dataset_group.serialize_aws_json_1_1(
                value["dataset_group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetGroupResponse:
    out: DescribeDatasetGroupResponse = {}  # type: ignore[typeddict-item]
    if "datasetGroup" in data:
        import capo_personalize.types.dataset_group

        out["dataset_group"] = (
            capo_personalize.types.dataset_group.deserialize_aws_json_1_1(
                data["datasetGroup"]
            )
        )
    return out
