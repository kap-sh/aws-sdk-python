"""Generated from Smithy shape ``com.amazonaws.codepipeline#WebhookList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.list_webhook_item

WebhookList: TypeAlias = list[
    "aws_sdk_codepipeline.types.list_webhook_item.ListWebhookItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebhookList) -> list:
    import aws_sdk_codepipeline.types.list_webhook_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codepipeline.types.list_webhook_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WebhookList:
    import aws_sdk_codepipeline.types.list_webhook_item

    out: WebhookList = []
    for item in data:
        out.append(
            aws_sdk_codepipeline.types.list_webhook_item.deserialize_aws_json_1_1(item)
        )
    return out
