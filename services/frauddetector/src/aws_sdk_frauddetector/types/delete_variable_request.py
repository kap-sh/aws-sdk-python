"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteVariableRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.string


class DeleteVariableRequest(TypedDict):
    name: "aws_sdk_frauddetector.types.string.string"
    """<p>The name of the variable to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteVariableRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteVariableRequest:
    out: DeleteVariableRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteVariableRequest.name required")
    return out
