"""Generated from Smithy shape ``com.amazonaws.amplify#Webhook``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app_id
    import aws_sdk_amplify.types.branch_name
    import aws_sdk_amplify.types.create_time
    import aws_sdk_amplify.types.description
    import aws_sdk_amplify.types.update_time
    import aws_sdk_amplify.types.webhook_arn
    import aws_sdk_amplify.types.webhook_id
    import aws_sdk_amplify.types.webhook_url


class Webhook(TypedDict):
    webhook_arn: "aws_sdk_amplify.types.webhook_arn.WebhookArn"
    """<p>The Amazon Resource Name (ARN) for the webhook. </p>"""
    webhook_id: "aws_sdk_amplify.types.webhook_id.WebhookId"
    """<p>The ID of the webhook. </p>"""
    webhook_url: "aws_sdk_amplify.types.webhook_url.WebhookUrl"
    """<p>The URL of the webhook. </p>"""
    app_id: NotRequired["aws_sdk_amplify.types.app_id.AppId"]
    """<p>The unique ID of an Amplify app.</p>"""
    branch_name: "aws_sdk_amplify.types.branch_name.BranchName"
    """<p>The name for a branch that is part of an Amplify app. </p>"""
    description: "aws_sdk_amplify.types.description.Description"
    """<p>The description for a webhook. </p>"""
    create_time: "aws_sdk_amplify.types.create_time.CreateTime"
    """<p>A timestamp of when Amplify created the webhook in your Git repository.</p>"""
    update_time: "aws_sdk_amplify.types.update_time.UpdateTime"
    """<p>A timestamp of when Amplify updated the webhook in your Git repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Webhook) -> dict:
    out: dict = {}
    out["webhookArn"] = value["webhook_arn"]
    out["webhookId"] = value["webhook_id"]
    out["webhookUrl"] = value["webhook_url"]
    if "app_id" in value:
        out["appId"] = value["app_id"]
    out["branchName"] = value["branch_name"]
    out["description"] = value["description"]
    import aws_sdk_amplify.types.create_time

    out["createTime"] = aws_sdk_amplify.types.create_time.serialize_json(
        value["create_time"]
    )
    import aws_sdk_amplify.types.update_time

    out["updateTime"] = aws_sdk_amplify.types.update_time.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> Webhook:
    out: Webhook = {}  # type: ignore[typeddict-item]
    if "webhookArn" in data:
        out["webhook_arn"] = data["webhookArn"]
    else:
        raise DeserializationError("Webhook.webhook_arn required")
    if "webhookId" in data:
        out["webhook_id"] = data["webhookId"]
    else:
        raise DeserializationError("Webhook.webhook_id required")
    if "webhookUrl" in data:
        out["webhook_url"] = data["webhookUrl"]
    else:
        raise DeserializationError("Webhook.webhook_url required")
    if "appId" in data:
        out["app_id"] = data["appId"]
    if "branchName" in data:
        out["branch_name"] = data["branchName"]
    else:
        raise DeserializationError("Webhook.branch_name required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("Webhook.description required")
    if "createTime" in data:
        import aws_sdk_amplify.types.create_time

        out["create_time"] = aws_sdk_amplify.types.create_time.deserialize_json(
            data["createTime"]
        )
    else:
        raise DeserializationError("Webhook.create_time required")
    if "updateTime" in data:
        import aws_sdk_amplify.types.update_time

        out["update_time"] = aws_sdk_amplify.types.update_time.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError("Webhook.update_time required")
    return out
