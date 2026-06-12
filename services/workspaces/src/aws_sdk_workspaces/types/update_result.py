"""Generated from Smithy shape ``com.amazonaws.workspaces#UpdateResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.boolean_object
    import aws_sdk_workspaces.types.update_description


class UpdateResult(TypedDict):
    update_available: NotRequired[
        "aws_sdk_workspaces.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether updated drivers or other components are available for the specified WorkSpace image.</p>"""
    description: NotRequired[
        "aws_sdk_workspaces.types.update_description.UpdateDescription"
    ]
    """<p>A description of whether updates for the WorkSpace image are pending or available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResult) -> dict:
    out: dict = {}
    if "update_available" in value:
        out["UpdateAvailable"] = value["update_available"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateResult:
    out: UpdateResult = {}  # type: ignore[typeddict-item]
    if "UpdateAvailable" in data:
        out["update_available"] = data["UpdateAvailable"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
