"""Generated from Smithy shape ``com.amazonaws.codepipeline#DeleteWebhookInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.webhook_name


class DeleteWebhookInput(TypedDict):
    name: "aws_sdk_codepipeline.types.webhook_name.WebhookName"
    """<p>The name of the webhook you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWebhookInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWebhookInput:
    out: DeleteWebhookInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteWebhookInput.name required")
    return out
