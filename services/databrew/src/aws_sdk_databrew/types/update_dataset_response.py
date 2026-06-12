"""Generated from Smithy shape ``com.amazonaws.databrew#UpdateDatasetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.dataset_name


class UpdateDatasetResponse(TypedDict):
    name: "aws_sdk_databrew.types.dataset_name.DatasetName"
    """<p>The name of the dataset that you updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDatasetResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateDatasetResponse:
    out: UpdateDatasetResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateDatasetResponse.name required")
    return out
