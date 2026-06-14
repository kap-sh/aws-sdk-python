"""Generated from Smithy shape ``com.amazonaws.connect#AttachedFile``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.created_by_info
    import aws_sdk_connect.types.file_id
    import aws_sdk_connect.types.file_name
    import aws_sdk_connect.types.file_size_in_bytes
    import aws_sdk_connect.types.file_status_type
    import aws_sdk_connect.types.file_use_case_type
    import aws_sdk_connect.types.iso8601_datetime
    import aws_sdk_connect.types.tag_map


class AttachedFile(TypedDict):
    creation_time: "aws_sdk_connect.types.iso8601_datetime.ISO8601Datetime"
    """<p>The time of Creation of the file resource as an ISO timestamp. It's specified in ISO 8601 format: <code>yyyy-MM-ddThh:mm:ss.SSSZ</code>. For example, <code>2024-05-03T02:41:28.172Z</code>.</p>"""
    file_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The unique identifier of the attached file resource (ARN).</p>"""
    file_id: "aws_sdk_connect.types.file_id.FileId"
    """<p>The unique identifier of the attached file resource.</p>"""
    file_name: "aws_sdk_connect.types.file_name.FileName"
    """<p>A case-sensitive name of the attached file being uploaded.</p>"""
    file_size_in_bytes: "aws_sdk_connect.types.file_size_in_bytes.FileSizeInBytes"
    """<p>The size of the attached file in bytes.</p>"""
    file_status: "aws_sdk_connect.types.file_status_type.FileStatusType"
    """<p>The current status of the attached file.</p>"""
    created_by: NotRequired["aws_sdk_connect.types.created_by_info.CreatedByInfo"]
    """<p>Represents the identity that created the file.</p>"""
    file_use_case_type: NotRequired[
        "aws_sdk_connect.types.file_use_case_type.FileUseCaseType"
    ]
    """<p>The use case for the file.</p>"""
    associated_resource_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    r"""<p>The resource to which the attached file is (being) uploaded to. <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateCase.html\">Cases</a> are the only current supported resource.</p> <note> <p>This value must be a valid ARN.</p> </note>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, <code>{ \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachedFile) -> dict:
    out: dict = {}
    out["CreationTime"] = value["creation_time"]
    out["FileArn"] = value["file_arn"]
    out["FileId"] = value["file_id"]
    out["FileName"] = value["file_name"]
    out["FileSizeInBytes"] = value["file_size_in_bytes"]
    import aws_sdk_connect.types.file_status_type

    out["FileStatus"] = aws_sdk_connect.types.file_status_type.serialize_json(
        value["file_status"]
    )
    if "created_by" in value:
        import aws_sdk_connect.types.created_by_info

        out["CreatedBy"] = aws_sdk_connect.types.created_by_info.serialize_json(
            value["created_by"]
        )
    if "file_use_case_type" in value:
        import aws_sdk_connect.types.file_use_case_type

        out["FileUseCaseType"] = (
            aws_sdk_connect.types.file_use_case_type.serialize_json(
                value["file_use_case_type"]
            )
        )
    if "associated_resource_arn" in value:
        out["AssociatedResourceArn"] = value["associated_resource_arn"]
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AttachedFile:
    out: AttachedFile = {}  # type: ignore[typeddict-item]
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    else:
        raise DeserializationError("AttachedFile.creation_time required")
    if "FileArn" in data:
        out["file_arn"] = data["FileArn"]
    else:
        raise DeserializationError("AttachedFile.file_arn required")
    if "FileId" in data:
        out["file_id"] = data["FileId"]
    else:
        raise DeserializationError("AttachedFile.file_id required")
    if "FileName" in data:
        out["file_name"] = data["FileName"]
    else:
        raise DeserializationError("AttachedFile.file_name required")
    if "FileSizeInBytes" in data:
        out["file_size_in_bytes"] = data["FileSizeInBytes"]
    else:
        raise DeserializationError("AttachedFile.file_size_in_bytes required")
    if "FileStatus" in data:
        import aws_sdk_connect.types.file_status_type

        out["file_status"] = aws_sdk_connect.types.file_status_type.deserialize_json(
            data["FileStatus"]
        )
    else:
        raise DeserializationError("AttachedFile.file_status required")
    if "CreatedBy" in data:
        import aws_sdk_connect.types.created_by_info

        out["created_by"] = aws_sdk_connect.types.created_by_info.deserialize_json(
            data["CreatedBy"]
        )
    if "FileUseCaseType" in data:
        import aws_sdk_connect.types.file_use_case_type

        out["file_use_case_type"] = (
            aws_sdk_connect.types.file_use_case_type.deserialize_json(
                data["FileUseCaseType"]
            )
        )
    if "AssociatedResourceArn" in data:
        out["associated_resource_arn"] = data["AssociatedResourceArn"]
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
