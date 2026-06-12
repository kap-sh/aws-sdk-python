"""Generated from Smithy shape ``com.amazonaws.glue#DeleteBlueprintRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class DeleteBlueprintRequest(TypedDict):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the blueprint to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBlueprintRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBlueprintRequest:
    out: DeleteBlueprintRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteBlueprintRequest.name required")
    return out
