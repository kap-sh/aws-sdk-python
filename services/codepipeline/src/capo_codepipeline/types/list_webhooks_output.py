"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListWebhooksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.next_token
    import capo_codepipeline.types.webhook_list


class ListWebhooksOutput(TypedDict, closed=True):
    webhooks: NotRequired["capo_codepipeline.types.webhook_list.WebhookList"]
    """<p>The JSON detail returned for each webhook in the list output for the ListWebhooks call.</p>"""
    next_token: NotRequired["capo_codepipeline.types.next_token.NextToken"]
    """<p>If the amount of returned information is significantly large, an identifier is also returned and can be used in a subsequent ListWebhooks call to return the next set of webhooks in the list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWebhooksOutput) -> dict:
    out: dict = {}
    if "webhooks" in value:
        import capo_codepipeline.types.webhook_list

        out["webhooks"] = capo_codepipeline.types.webhook_list.serialize_aws_json_1_1(
            value["webhooks"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWebhooksOutput:
    out: ListWebhooksOutput = {}  # type: ignore[typeddict-item]
    if "webhooks" in data:
        import capo_codepipeline.types.webhook_list

        out["webhooks"] = capo_codepipeline.types.webhook_list.deserialize_aws_json_1_1(
            data["webhooks"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
