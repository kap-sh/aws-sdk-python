"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#TransformationTool``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.tranformation_tool_description
    import aws_sdk_migrationhubstrategy.types.tranformation_tool_installation_link
    import aws_sdk_migrationhubstrategy.types.transformation_tool_name


class TransformationTool(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_migrationhubstrategy.types.transformation_tool_name.TransformationToolName"
    ]
    """<p> Name of the tool. </p>"""
    description: NotRequired[
        "aws_sdk_migrationhubstrategy.types.tranformation_tool_description.TranformationToolDescription"
    ]
    """<p> Description of the tool. </p>"""
    tranformation_tool_installation_link: NotRequired[
        "aws_sdk_migrationhubstrategy.types.tranformation_tool_installation_link.TranformationToolInstallationLink"
    ]
    """<p> URL for installing the tool. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransformationTool) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tranformation_tool_installation_link" in value:
        out["tranformationToolInstallationLink"] = value[
            "tranformation_tool_installation_link"
        ]
    return out


def deserialize_json(data: dict) -> TransformationTool:
    out: TransformationTool = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "tranformationToolInstallationLink" in data:
        out["tranformation_tool_installation_link"] = data[
            "tranformationToolInstallationLink"
        ]
    return out
