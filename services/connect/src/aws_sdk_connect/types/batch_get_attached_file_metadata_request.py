"""Generated from Smithy shape ``com.amazonaws.connect#BatchGetAttachedFileMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.file_id_list
    import aws_sdk_connect.types.instance_id


class BatchGetAttachedFileMetadataRequest(TypedDict, closed=True):
    file_ids: "aws_sdk_connect.types.file_id_list.FileIdList"
    """<p>The unique identifiers of the attached file resource.</p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The unique identifier of the Connect instance.</p>"""
    associated_resource_arn: "aws_sdk_connect.types.arn.ARN"
    r"""<p>The resource to which the attached file is (being) uploaded to. The supported resources are <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/cases.html\">Cases</a> and <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/setup-email-channel.html\">Email</a>.</p> <note> <p>This value must be a valid ARN.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAttachedFileMetadataRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.file_id_list

    out["FileIds"] = aws_sdk_connect.types.file_id_list.serialize_json(
        value["file_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetAttachedFileMetadataRequest:
    out: BatchGetAttachedFileMetadataRequest = {}  # type: ignore[typeddict-item]
    if "FileIds" in data:
        import aws_sdk_connect.types.file_id_list

        out["file_ids"] = aws_sdk_connect.types.file_id_list.deserialize_json(
            data["FileIds"]
        )
    else:
        raise DeserializationError(
            "BatchGetAttachedFileMetadataRequest.file_ids required"
        )
    return out
