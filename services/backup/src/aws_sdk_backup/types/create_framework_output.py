"""Generated from Smithy shape ``com.amazonaws.backup#CreateFrameworkOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.framework_name

class CreateFrameworkOutput(TypedDict):
    framework_name: NotRequired["aws_sdk_backup.types.framework_name.FrameworkName"]
    """<p>The unique name of the framework. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).</p>"""
    framework_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateFrameworkOutput) -> dict:
    out: dict = {}
    if "framework_name" in value:
        out["FrameworkName"] = value["framework_name"]
    if "framework_arn" in value:
        out["FrameworkArn"] = value["framework_arn"]
    return out


def deserialize_json(data: dict) -> CreateFrameworkOutput:
    out: CreateFrameworkOutput = {}  # type: ignore[typeddict-item]
    if "FrameworkName" in data:
        out["framework_name"] = data["FrameworkName"]
    if "FrameworkArn" in data:
        out["framework_arn"] = data["FrameworkArn"]
    return out