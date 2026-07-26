"""Generated from Smithy shape ``com.amazonaws.supportapp#SlackWorkspaceConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_support_app.types.slack_workspace_configuration

SlackWorkspaceConfigurationList: TypeAlias = list[
    "capo_support_app.types.slack_workspace_configuration.SlackWorkspaceConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlackWorkspaceConfigurationList) -> list:
    import capo_support_app.types.slack_workspace_configuration

    out: list = []
    for item in value:
        out.append(
            capo_support_app.types.slack_workspace_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SlackWorkspaceConfigurationList:
    import capo_support_app.types.slack_workspace_configuration

    out: SlackWorkspaceConfigurationList = []
    for item in data:
        out.append(
            capo_support_app.types.slack_workspace_configuration.deserialize_json(item)
        )
    return out
