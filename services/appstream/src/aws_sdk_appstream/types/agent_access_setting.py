"""Generated from Smithy shape ``com.amazonaws.appstream#AgentAccessSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.agent_action
    import aws_sdk_appstream.types.permission


class AgentAccessSetting(TypedDict, closed=True):
    agent_action: NotRequired["aws_sdk_appstream.types.agent_action.AgentAction"]
    """<p>The agent action to configure. Valid values are COMPUTER_VISION and COMPUTER_INPUT. If you enable COMPUTER_INPUT, you must also enable COMPUTER_VISION.</p>"""
    permission: NotRequired["aws_sdk_appstream.types.permission.Permission"]
    """<p>Whether the agent action is enabled or disabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentAccessSetting) -> dict:
    out: dict = {}
    if "agent_action" in value:
        import aws_sdk_appstream.types.agent_action

        out["AgentAction"] = (
            aws_sdk_appstream.types.agent_action.serialize_aws_json_1_1(
                value["agent_action"]
            )
        )
    if "permission" in value:
        import aws_sdk_appstream.types.permission

        out["Permission"] = aws_sdk_appstream.types.permission.serialize_aws_json_1_1(
            value["permission"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AgentAccessSetting:
    out: AgentAccessSetting = {}  # type: ignore[typeddict-item]
    if "AgentAction" in data:
        import aws_sdk_appstream.types.agent_action

        out["agent_action"] = (
            aws_sdk_appstream.types.agent_action.deserialize_aws_json_1_1(
                data["AgentAction"]
            )
        )
    if "Permission" in data:
        import aws_sdk_appstream.types.permission

        out["permission"] = aws_sdk_appstream.types.permission.deserialize_aws_json_1_1(
            data["Permission"]
        )
    return out
