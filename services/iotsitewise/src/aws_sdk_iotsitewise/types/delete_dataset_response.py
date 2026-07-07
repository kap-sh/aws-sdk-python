"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.dataset_status


class DeleteDatasetResponse(TypedDict, closed=True):
    dataset_status: "aws_sdk_iotsitewise.types.dataset_status.DatasetStatus"
    """<p>The status of the dataset. This contains the state and any error messages. State is <code>DELETING</code> after a successfull call to this API, and any associated error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDatasetResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.dataset_status

    out["datasetStatus"] = aws_sdk_iotsitewise.types.dataset_status.serialize_json(
        value["dataset_status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteDatasetResponse:
    out: DeleteDatasetResponse = {}  # type: ignore[typeddict-item]
    if "datasetStatus" in data:
        import aws_sdk_iotsitewise.types.dataset_status

        out["dataset_status"] = (
            aws_sdk_iotsitewise.types.dataset_status.deserialize_json(
                data["datasetStatus"]
            )
        )
    else:
        raise DeserializationError("DeleteDatasetResponse.dataset_status required")
    return out
