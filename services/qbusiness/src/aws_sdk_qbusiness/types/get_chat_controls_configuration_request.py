"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetChatControlsConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.max_results_integer_for_get_topic_configurations
    import aws_sdk_qbusiness.types.next_token


class GetChatControlsConfigurationRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application for which the chat controls are configured.</p>"""
    max_results: NotRequired[
        "aws_sdk_qbusiness.types.max_results_integer_for_get_topic_configurations.MaxResultsIntegerForGetTopicConfigurations"
    ]
    """<p>The maximum number of configured chat controls to return.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business chat controls configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChatControlsConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetChatControlsConfigurationRequest:
    out: GetChatControlsConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
