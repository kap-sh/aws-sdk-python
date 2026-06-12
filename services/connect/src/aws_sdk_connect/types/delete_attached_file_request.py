"""Generated from Smithy shape ``com.amazonaws.connect#DeleteAttachedFileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.file_id
    import aws_sdk_connect.types.instance_id


class DeleteAttachedFileRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The unique identifier of the Connect instance.</p>"""
    file_id: "aws_sdk_connect.types.file_id.FileId"
    """<p>The unique identifier of the attached file resource.</p>"""
    associated_resource_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The resource to which the attached file is (being) uploaded to. <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateCase.html\">Cases</a> are the only current supported resource.</p> <note> <p>This value must be a valid ARN.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAttachedFileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAttachedFileRequest:
    out: DeleteAttachedFileRequest = {}  # type: ignore[typeddict-item]
    return out
