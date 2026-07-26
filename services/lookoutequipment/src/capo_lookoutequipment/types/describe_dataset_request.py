"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lookoutequipment.types.dataset_identifier


class DescribeDatasetRequest(TypedDict, closed=True):
    dataset_name: "capo_lookoutequipment.types.dataset_identifier.DatasetIdentifier"
    """<p>The name of the dataset to be described. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeDatasetRequest) -> dict:
    out: dict = {}
    out["DatasetName"] = value["dataset_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeDatasetRequest:
    out: DescribeDatasetRequest = {}  # type: ignore[typeddict-item]
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    else:
        raise DeserializationError("DescribeDatasetRequest.dataset_name required")
    return out
