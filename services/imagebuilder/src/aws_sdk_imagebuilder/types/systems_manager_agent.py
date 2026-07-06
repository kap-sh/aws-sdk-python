"""Generated from Smithy shape ``com.amazonaws.imagebuilder#SystemsManagerAgent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.nullable_boolean


class SystemsManagerAgent(TypedDict, closed=True):
    uninstall_after_build: NotRequired[
        "aws_sdk_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Controls whether the Systems Manager agent is removed from your final build image, prior to creating the new AMI. If this is set to true, then the agent is removed from the final image. If it's set to false, then the agent is left in, so that it is included in the new AMI. default value is false.</p> <p>The default behavior of uninstallAfterBuild is to remove the SSM Agent if it was installed by EC2 Image Builder</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemsManagerAgent) -> dict:
    out: dict = {}
    if "uninstall_after_build" in value:
        out["uninstallAfterBuild"] = value["uninstall_after_build"]
    return out


def deserialize_json(data: dict) -> SystemsManagerAgent:
    out: SystemsManagerAgent = {}  # type: ignore[typeddict-item]
    if "uninstallAfterBuild" in data:
        out["uninstall_after_build"] = data["uninstallAfterBuild"]
    return out
