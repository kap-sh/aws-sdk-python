"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.no_dash_identifier


class DeleteListRequest(TypedDict, closed=True):
    name: "capo_frauddetector.types.no_dash_identifier.noDashIdentifier"
    """<p> The name of the list to delete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteListRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteListRequest:
    out: DeleteListRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteListRequest.name required")
    return out
