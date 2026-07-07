"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DeleteDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.dataset_identifier


class DeleteDatasetRequest(TypedDict, closed=True):
    dataset_name: "aws_sdk_lookoutequipment.types.dataset_identifier.DatasetIdentifier"
    """<p>The name of the dataset to be deleted. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteDatasetRequest) -> dict:
    out: dict = {}
    out["DatasetName"] = value["dataset_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteDatasetRequest:
    out: DeleteDatasetRequest = {}  # type: ignore[typeddict-item]
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    else:
        raise DeserializationError("DeleteDatasetRequest.dataset_name required")
    return out
