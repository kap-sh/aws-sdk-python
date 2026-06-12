"""Generated from Smithy shape ``com.amazonaws.glue#DeleteBlueprintResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class DeleteBlueprintResponse(TypedDict):
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>Returns the name of the blueprint that was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBlueprintResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBlueprintResponse:
    out: DeleteBlueprintResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
