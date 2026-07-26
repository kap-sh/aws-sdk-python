"""Generated from Smithy shape ``com.amazonaws.clouddirectory#CreateDirectoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.directory_arn
    import capo_clouddirectory.types.directory_name
    import capo_clouddirectory.types.object_identifier


class CreateDirectoryResponse(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.directory_arn.DirectoryArn"
    """<p>The ARN that is associated with the <a>Directory</a>. For more information, see <a>arns</a>.</p>"""
    name: "capo_clouddirectory.types.directory_name.DirectoryName"
    """<p>The name of the <a>Directory</a>.</p>"""
    object_identifier: "capo_clouddirectory.types.object_identifier.ObjectIdentifier"
    """<p>The root object node of the created directory.</p>"""
    applied_schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The ARN of the published schema in the <a>Directory</a>. Once a published schema is copied into the directory, it has its own ARN, which is referred to applied schema ARN. For more information, see <a>arns</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDirectoryResponse) -> dict:
    out: dict = {}
    out["DirectoryArn"] = value["directory_arn"]
    out["Name"] = value["name"]
    out["ObjectIdentifier"] = value["object_identifier"]
    out["AppliedSchemaArn"] = value["applied_schema_arn"]
    return out


def deserialize_json(data: dict) -> CreateDirectoryResponse:
    out: CreateDirectoryResponse = {}  # type: ignore[typeddict-item]
    if "DirectoryArn" in data:
        out["directory_arn"] = data["DirectoryArn"]
    else:
        raise DeserializationError("CreateDirectoryResponse.directory_arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDirectoryResponse.name required")
    if "ObjectIdentifier" in data:
        out["object_identifier"] = data["ObjectIdentifier"]
    else:
        raise DeserializationError("CreateDirectoryResponse.object_identifier required")
    if "AppliedSchemaArn" in data:
        out["applied_schema_arn"] = data["AppliedSchemaArn"]
    else:
        raise DeserializationError(
            "CreateDirectoryResponse.applied_schema_arn required"
        )
    return out
