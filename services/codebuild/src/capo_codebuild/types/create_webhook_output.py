"""Generated from Smithy shape ``com.amazonaws.codebuild#CreateWebhookOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.webhook


class CreateWebhookOutput(TypedDict, closed=True):
    webhook: NotRequired["capo_codebuild.types.webhook.Webhook"]
    """<p>Information about a webhook that connects repository events to a build project in CodeBuild.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWebhookOutput) -> dict:
    out: dict = {}
    if "webhook" in value:
        import capo_codebuild.types.webhook

        out["webhook"] = capo_codebuild.types.webhook.serialize_aws_json_1_1(
            value["webhook"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWebhookOutput:
    out: CreateWebhookOutput = {}  # type: ignore[typeddict-item]
    if "webhook" in data:
        import capo_codebuild.types.webhook

        out["webhook"] = capo_codebuild.types.webhook.deserialize_aws_json_1_1(
            data["webhook"]
        )
    return out
