"""Generated from Smithy shape ``com.amazonaws.glue#DeleteCustomEntityTypeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class DeleteCustomEntityTypeResponse(TypedDict):
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the custom pattern you deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCustomEntityTypeResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCustomEntityTypeResponse:
    out: DeleteCustomEntityTypeResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
