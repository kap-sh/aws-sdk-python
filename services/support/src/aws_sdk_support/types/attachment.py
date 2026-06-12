"""Generated from Smithy shape ``com.amazonaws.support#Attachment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_support.types.data
    import aws_sdk_support.types.file_name


class Attachment(TypedDict):
    file_name: NotRequired["aws_sdk_support.types.file_name.FileName"]
    """<p>The name of the attachment file.</p>"""
    data: NotRequired["aws_sdk_support.types.data.Data"]
    """<p>The content of the attachment file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Attachment) -> dict:
    out: dict = {}
    if "file_name" in value:
        out["fileName"] = value["file_name"]
    if "data" in value:
        import aws_sdk_support.types.data

        out["data"] = aws_sdk_support.types.data.serialize_aws_json_1_1(value["data"])
    return out


def deserialize_aws_json_1_1(data: dict) -> Attachment:
    out: Attachment = {}  # type: ignore[typeddict-item]
    if "fileName" in data:
        out["file_name"] = data["fileName"]
    if "data" in data:
        import aws_sdk_support.types.data

        out["data"] = aws_sdk_support.types.data.deserialize_aws_json_1_1(data["data"])
    return out
