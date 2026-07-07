"""Generated from Smithy shape ``com.amazonaws.amplify#UpdateWebhookRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplify.types.branch_name
    import aws_sdk_amplify.types.description
    import aws_sdk_amplify.types.webhook_id


class UpdateWebhookRequest(TypedDict, closed=True):
    webhook_id: "aws_sdk_amplify.types.webhook_id.WebhookId"
    """<p>The unique ID for a webhook. </p>"""
    branch_name: NotRequired["aws_sdk_amplify.types.branch_name.BranchName"]
    """<p>The name for a branch that is part of an Amplify app. </p>"""
    description: NotRequired["aws_sdk_amplify.types.description.Description"]
    """<p>The description for a webhook. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWebhookRequest) -> dict:
    out: dict = {}
    if "branch_name" in value:
        out["branchName"] = value["branch_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateWebhookRequest:
    out: UpdateWebhookRequest = {}  # type: ignore[typeddict-item]
    if "branchName" in data:
        out["branch_name"] = data["branchName"]
    if "description" in data:
        out["description"] = data["description"]
    return out
