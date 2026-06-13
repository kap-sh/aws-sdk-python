"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetArchiveMessageContentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.message_body


class GetArchiveMessageContentResponse(TypedDict):
    body: NotRequired["aws_sdk_mailmanager.types.message_body.MessageBody"]
    """<p>The textual body content of the email message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetArchiveMessageContentResponse) -> dict:
    out: dict = {}
    if "body" in value:
        import aws_sdk_mailmanager.types.message_body

        out["Body"] = aws_sdk_mailmanager.types.message_body.serialize_aws_json_1_0(
            value["body"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetArchiveMessageContentResponse:
    out: GetArchiveMessageContentResponse = {}  # type: ignore[typeddict-item]
    if "Body" in data:
        import aws_sdk_mailmanager.types.message_body

        out["body"] = aws_sdk_mailmanager.types.message_body.deserialize_aws_json_1_0(
            data["Body"]
        )
    return out
