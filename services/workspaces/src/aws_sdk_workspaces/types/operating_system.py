"""Generated from Smithy shape ``com.amazonaws.workspaces#OperatingSystem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.operating_system_type


class OperatingSystem(TypedDict):
    type: NotRequired[
        "aws_sdk_workspaces.types.operating_system_type.OperatingSystemType"
    ]
    """<p>The operating system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperatingSystem) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_workspaces.types.operating_system_type

        out["Type"] = (
            aws_sdk_workspaces.types.operating_system_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OperatingSystem:
    out: OperatingSystem = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_workspaces.types.operating_system_type

        out["type"] = (
            aws_sdk_workspaces.types.operating_system_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    return out
