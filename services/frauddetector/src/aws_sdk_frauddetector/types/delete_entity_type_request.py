"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteEntityTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.identifier


class DeleteEntityTypeRequest(TypedDict):
    name: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The name of the entity type to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEntityTypeRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEntityTypeRequest:
    out: DeleteEntityTypeRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteEntityTypeRequest.name required")
    return out
