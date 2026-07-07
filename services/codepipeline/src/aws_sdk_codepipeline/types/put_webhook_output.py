"""Generated from Smithy shape ``com.amazonaws.codepipeline#PutWebhookOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.list_webhook_item


class PutWebhookOutput(TypedDict, closed=True):
    webhook: NotRequired["aws_sdk_codepipeline.types.list_webhook_item.ListWebhookItem"]
    """<p>The detail returned from creating the webhook, such as the webhook name, webhook URL, and webhook ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutWebhookOutput) -> dict:
    out: dict = {}
    if "webhook" in value:
        import aws_sdk_codepipeline.types.list_webhook_item

        out["webhook"] = (
            aws_sdk_codepipeline.types.list_webhook_item.serialize_aws_json_1_1(
                value["webhook"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutWebhookOutput:
    out: PutWebhookOutput = {}  # type: ignore[typeddict-item]
    if "webhook" in data:
        import aws_sdk_codepipeline.types.list_webhook_item

        out["webhook"] = (
            aws_sdk_codepipeline.types.list_webhook_item.deserialize_aws_json_1_1(
                data["webhook"]
            )
        )
    return out
