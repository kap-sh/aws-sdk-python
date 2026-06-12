"""Generated from Smithy shape ``com.amazonaws.amplify#DeleteWebhookResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.webhook


class DeleteWebhookResult(TypedDict):
    webhook: "aws_sdk_amplify.types.webhook.Webhook"
    """<p>Describes a webhook that connects repository events to an Amplify app. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWebhookResult) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.webhook

    out["webhook"] = aws_sdk_amplify.types.webhook.serialize_json(value["webhook"])
    return out


def deserialize_json(data: dict) -> DeleteWebhookResult:
    out: DeleteWebhookResult = {}  # type: ignore[typeddict-item]
    if "webhook" in data:
        import aws_sdk_amplify.types.webhook

        out["webhook"] = aws_sdk_amplify.types.webhook.deserialize_json(data["webhook"])
    else:
        raise DeserializationError("DeleteWebhookResult.webhook required")
    return out
