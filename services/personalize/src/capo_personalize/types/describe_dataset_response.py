"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.dataset


class DescribeDatasetResponse(TypedDict, closed=True):
    dataset: NotRequired["capo_personalize.types.dataset.Dataset"]
    """<p>A listing of the dataset's properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetResponse) -> dict:
    out: dict = {}
    if "dataset" in value:
        import capo_personalize.types.dataset

        out["dataset"] = capo_personalize.types.dataset.serialize_aws_json_1_1(
            value["dataset"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetResponse:
    out: DescribeDatasetResponse = {}  # type: ignore[typeddict-item]
    if "dataset" in data:
        import capo_personalize.types.dataset

        out["dataset"] = capo_personalize.types.dataset.deserialize_aws_json_1_1(
            data["dataset"]
        )
    return out
