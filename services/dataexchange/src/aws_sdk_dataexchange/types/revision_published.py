"""Generated from Smithy shape ``com.amazonaws.dataexchange#RevisionPublished``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.id


class RevisionPublished(TypedDict):
    data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The data set ID of the published revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevisionPublished) -> dict:
    out: dict = {}
    out["DataSetId"] = value["data_set_id"]
    return out


def deserialize_json(data: dict) -> RevisionPublished:
    out: RevisionPublished = {}  # type: ignore[typeddict-item]
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError("RevisionPublished.data_set_id required")
    return out
