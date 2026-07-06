"""Generated from Smithy shape ``com.amazonaws.databrew#DeleteDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.dataset_name


class DeleteDatasetResponse(TypedDict, closed=True):
    name: "aws_sdk_databrew.types.dataset_name.DatasetName"
    """<p>The name of the dataset that you deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDatasetResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteDatasetResponse:
    out: DeleteDatasetResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteDatasetResponse.name required")
    return out
