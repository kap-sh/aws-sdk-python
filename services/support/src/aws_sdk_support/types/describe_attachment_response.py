"""Generated from Smithy shape ``com.amazonaws.support#DescribeAttachmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_support.types.attachment


class DescribeAttachmentResponse(TypedDict):
    attachment: NotRequired["aws_sdk_support.types.attachment.Attachment"]
    """<p>This object includes the attachment content and file name.</p> <p>In the previous response syntax, the value for the <code>data</code> parameter appears as <code>blob</code>, which is represented as a base64-encoded string. The value for <code>fileName</code> is the name of the attachment, such as <code>troubleshoot-screenshot.png</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAttachmentResponse) -> dict:
    out: dict = {}
    if "attachment" in value:
        import aws_sdk_support.types.attachment

        out["attachment"] = aws_sdk_support.types.attachment.serialize_aws_json_1_1(
            value["attachment"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAttachmentResponse:
    out: DescribeAttachmentResponse = {}  # type: ignore[typeddict-item]
    if "attachment" in data:
        import aws_sdk_support.types.attachment

        out["attachment"] = aws_sdk_support.types.attachment.deserialize_aws_json_1_1(
            data["attachment"]
        )
    return out
