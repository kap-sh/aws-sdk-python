"""Generated from Smithy shape ``com.amazonaws.directoryservice#StartSchemaExtensionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.create_snapshot_before_schema_extension
    import aws_sdk_directory_service.types.description
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.ldif_content


class StartSchemaExtensionRequest(TypedDict, closed=True):
    directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory for which the schema extension will be applied to.</p>"""
    create_snapshot_before_schema_extension: "aws_sdk_directory_service.types.create_snapshot_before_schema_extension.CreateSnapshotBeforeSchemaExtension"
    """<p>If true, creates a snapshot of the directory before applying the schema extension.</p>"""
    ldif_content: "aws_sdk_directory_service.types.ldif_content.LdifContent"
    r"""<p>The LDIF file represented as a string. To construct the LdifContent string, precede each line as it would be formatted in an ldif file with \n. See the example request below for more details. The file size can be no larger than 1MB.</p>"""
    description: "aws_sdk_directory_service.types.description.Description"
    """<p>A description of the schema extension.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSchemaExtensionRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["CreateSnapshotBeforeSchemaExtension"] = value.get(
        "create_snapshot_before_schema_extension", False
    )
    out["LdifContent"] = value["ldif_content"]
    out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSchemaExtensionRequest:
    out: StartSchemaExtensionRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("StartSchemaExtensionRequest.directory_id required")
    if "CreateSnapshotBeforeSchemaExtension" in data:
        out["create_snapshot_before_schema_extension"] = data[
            "CreateSnapshotBeforeSchemaExtension"
        ]
    else:
        out["create_snapshot_before_schema_extension"] = False
    if "LdifContent" in data:
        out["ldif_content"] = data["LdifContent"]
    else:
        raise DeserializationError("StartSchemaExtensionRequest.ldif_content required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("StartSchemaExtensionRequest.description required")
    return out
