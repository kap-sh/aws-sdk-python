"""Generated from Smithy shape ``com.amazonaws.datasync#Platform``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.agent_version


class Platform(TypedDict):
    version: NotRequired["aws_sdk_datasync.types.agent_version.AgentVersion"]
    """<p>The version of the DataSync agent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Platform) -> dict:
    out: dict = {}
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Platform:
    out: Platform = {}  # type: ignore[typeddict-item]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
