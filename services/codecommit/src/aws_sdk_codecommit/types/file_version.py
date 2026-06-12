"""Generated from Smithy shape ``com.amazonaws.codecommit#FileVersion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.commit
    import aws_sdk_codecommit.types.object_id
    import aws_sdk_codecommit.types.path
    import aws_sdk_codecommit.types.revision_children


class FileVersion(TypedDict):
    commit: NotRequired["aws_sdk_codecommit.types.commit.Commit"]
    blob_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>The blob ID of the object that represents the content of the file in this version.</p>"""
    path: NotRequired["aws_sdk_codecommit.types.path.Path"]
    """<p>The name and path of the file at which this blob is indexed which contains the data for this version of the file. This value will vary between file versions if a file is renamed or if its path changes.</p>"""
    revision_children: NotRequired[
        "aws_sdk_codecommit.types.revision_children.RevisionChildren"
    ]
    """<p>An array of commit IDs that contain more recent versions of this file. If there are no additional versions of the file, this array will be empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileVersion) -> dict:
    out: dict = {}
    if "commit" in value:
        import aws_sdk_codecommit.types.commit

        out["commit"] = aws_sdk_codecommit.types.commit.serialize_aws_json_1_1(
            value["commit"]
        )
    if "blob_id" in value:
        out["blobId"] = value["blob_id"]
    if "path" in value:
        out["path"] = value["path"]
    if "revision_children" in value:
        import aws_sdk_codecommit.types.revision_children

        out["revisionChildren"] = (
            aws_sdk_codecommit.types.revision_children.serialize_aws_json_1_1(
                value["revision_children"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FileVersion:
    out: FileVersion = {}  # type: ignore[typeddict-item]
    if "commit" in data:
        import aws_sdk_codecommit.types.commit

        out["commit"] = aws_sdk_codecommit.types.commit.deserialize_aws_json_1_1(
            data["commit"]
        )
    if "blobId" in data:
        out["blob_id"] = data["blobId"]
    if "path" in data:
        out["path"] = data["path"]
    if "revisionChildren" in data:
        import aws_sdk_codecommit.types.revision_children

        out["revision_children"] = (
            aws_sdk_codecommit.types.revision_children.deserialize_aws_json_1_1(
                data["revisionChildren"]
            )
        )
    return out
