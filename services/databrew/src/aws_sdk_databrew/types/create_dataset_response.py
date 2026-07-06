"""Generated from Smithy shape ``com.amazonaws.databrew#CreateDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.dataset_name


class CreateDatasetResponse(TypedDict, closed=True):
    name: "aws_sdk_databrew.types.dataset_name.DatasetName"
    """<p>The name of the dataset that you created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatasetResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateDatasetResponse:
    out: CreateDatasetResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDatasetResponse.name required")
    return out
