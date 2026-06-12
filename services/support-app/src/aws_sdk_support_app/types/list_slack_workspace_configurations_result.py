"""Generated from Smithy shape ``com.amazonaws.supportapp#ListSlackWorkspaceConfigurationsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_support_app.types.pagination_token
    import aws_sdk_support_app.types.slack_workspace_configuration_list


class ListSlackWorkspaceConfigurationsResult(TypedDict):
    next_token: NotRequired[
        "aws_sdk_support_app.types.pagination_token.paginationToken"
    ]
    """<p>The point where pagination should resume when the response returns only partial results.</p>"""
    slack_workspace_configurations: NotRequired[
        "aws_sdk_support_app.types.slack_workspace_configuration_list.SlackWorkspaceConfigurationList"
    ]
    """<p>The configurations for a Slack workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSlackWorkspaceConfigurationsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "slack_workspace_configurations" in value:
        import aws_sdk_support_app.types.slack_workspace_configuration_list

        out["slackWorkspaceConfigurations"] = (
            aws_sdk_support_app.types.slack_workspace_configuration_list.serialize_json(
                value["slack_workspace_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSlackWorkspaceConfigurationsResult:
    out: ListSlackWorkspaceConfigurationsResult = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "slackWorkspaceConfigurations" in data:
        import aws_sdk_support_app.types.slack_workspace_configuration_list

        out["slack_workspace_configurations"] = (
            aws_sdk_support_app.types.slack_workspace_configuration_list.deserialize_json(
                data["slackWorkspaceConfigurations"]
            )
        )
    return out
