"""Generated from Smithy shape ``com.amazonaws.supportapp#ListSlackChannelConfigurationsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_support_app.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support_app.types.pagination_token
    import aws_sdk_support_app.types.slack_channel_configuration_list


class ListSlackChannelConfigurationsResult(TypedDict):
    next_token: NotRequired[
        "aws_sdk_support_app.types.pagination_token.paginationToken"
    ]
    """<p>The point where pagination should resume when the response returns only partial results.</p>"""
    slack_channel_configurations: "aws_sdk_support_app.types.slack_channel_configuration_list.slackChannelConfigurationList"
    """<p>The configurations for a Slack channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSlackChannelConfigurationsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_support_app.types.slack_channel_configuration_list

    out["slackChannelConfigurations"] = (
        aws_sdk_support_app.types.slack_channel_configuration_list.serialize_json(
            value["slack_channel_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListSlackChannelConfigurationsResult:
    out: ListSlackChannelConfigurationsResult = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "slackChannelConfigurations" in data:
        import aws_sdk_support_app.types.slack_channel_configuration_list

        out["slack_channel_configurations"] = (
            aws_sdk_support_app.types.slack_channel_configuration_list.deserialize_json(
                data["slackChannelConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "ListSlackChannelConfigurationsResult.slack_channel_configurations required"
        )
    return out
