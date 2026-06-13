"""Generated from Smithy shape ``com.amazonaws.omics#StartReadSetActivationJobSourceItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.read_set_id


class StartReadSetActivationJobSourceItem(TypedDict):
    read_set_id: "aws_sdk_omics.types.read_set_id.ReadSetId"
    """<p>The source's read set ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartReadSetActivationJobSourceItem) -> dict:
    out: dict = {}
    out["readSetId"] = value["read_set_id"]
    return out


def deserialize_json(data: dict) -> StartReadSetActivationJobSourceItem:
    out: StartReadSetActivationJobSourceItem = {}  # type: ignore[typeddict-item]
    if "readSetId" in data:
        out["read_set_id"] = data["readSetId"]
    else:
        raise DeserializationError(
            "StartReadSetActivationJobSourceItem.read_set_id required"
        )
    return out
