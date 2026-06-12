"""Generated from Smithy shape ``com.amazonaws.amplify#GetWebhookResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.webhook


class GetWebhookResult(TypedDict):
    webhook: "aws_sdk_amplify.types.webhook.Webhook"
    """<p>Describes the structure of a webhook. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWebhookResult) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.webhook

    out["webhook"] = aws_sdk_amplify.types.webhook.serialize_json(value["webhook"])
    return out


def deserialize_json(data: dict) -> GetWebhookResult:
    out: GetWebhookResult = {}  # type: ignore[typeddict-item]
    if "webhook" in data:
        import aws_sdk_amplify.types.webhook

        out["webhook"] = aws_sdk_amplify.types.webhook.deserialize_json(data["webhook"])
    else:
        raise DeserializationError("GetWebhookResult.webhook required")
    return out
