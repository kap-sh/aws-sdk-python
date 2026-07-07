"""Generated from Smithy shape ``com.amazonaws.appstream#StartImageBuilderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.appstream_agent_version
    import aws_sdk_appstream.types.string


class StartImageBuilderRequest(TypedDict, closed=True):
    name: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The name of the image builder.</p>"""
    appstream_agent_version: NotRequired[
        "aws_sdk_appstream.types.appstream_agent_version.AppstreamAgentVersion"
    ]
    """<p>The version of the WorkSpaces Applications agent to use for this image builder. To use the latest version of the WorkSpaces Applications agent, specify [LATEST]. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartImageBuilderRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "appstream_agent_version" in value:
        out["AppstreamAgentVersion"] = value["appstream_agent_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartImageBuilderRequest:
    out: StartImageBuilderRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "AppstreamAgentVersion" in data:
        out["appstream_agent_version"] = data["AppstreamAgentVersion"]
    return out
