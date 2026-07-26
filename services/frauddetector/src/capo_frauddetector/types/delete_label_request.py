"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteLabelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.identifier


class DeleteLabelRequest(TypedDict, closed=True):
    name: "capo_frauddetector.types.identifier.identifier"
    """<p>The name of the label to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLabelRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLabelRequest:
    out: DeleteLabelRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteLabelRequest.name required")
    return out
