"""Generated from Smithy shape ``com.amazonaws.rekognition#DistributeDatasetEntriesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.distribute_dataset_metadata_list


class DistributeDatasetEntriesRequest(TypedDict):
    datasets: "aws_sdk_rekognition.types.distribute_dataset_metadata_list.DistributeDatasetMetadataList"
    """<p>The ARNS for the training dataset and test dataset that you want to use. The datasets must belong to the same project. The test dataset must be empty. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DistributeDatasetEntriesRequest) -> dict:
    out: dict = {}
    import aws_sdk_rekognition.types.distribute_dataset_metadata_list

    out["Datasets"] = (
        aws_sdk_rekognition.types.distribute_dataset_metadata_list.serialize_aws_json_1_1(
            value["datasets"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DistributeDatasetEntriesRequest:
    out: DistributeDatasetEntriesRequest = {}  # type: ignore[typeddict-item]
    if "Datasets" in data:
        import aws_sdk_rekognition.types.distribute_dataset_metadata_list

        out["datasets"] = (
            aws_sdk_rekognition.types.distribute_dataset_metadata_list.deserialize_aws_json_1_1(
                data["Datasets"]
            )
        )
    else:
        raise DeserializationError("DistributeDatasetEntriesRequest.datasets required")
    return out
