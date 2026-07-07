"""Generated from Smithy shape ``com.amazonaws.codeconnections#Revision``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.branch_name
    import aws_sdk_codeconnections.types.directory
    import aws_sdk_codeconnections.types.owner_id
    import aws_sdk_codeconnections.types.provider_type
    import aws_sdk_codeconnections.types.repository_name
    import aws_sdk_codeconnections.types.sha


class Revision(TypedDict, closed=True):
    branch: "aws_sdk_codeconnections.types.branch_name.BranchName"
    """<p>The branch name for a specific revision.</p>"""
    directory: "aws_sdk_codeconnections.types.directory.Directory"
    """<p>The directory, if any, for a specific revision.</p>"""
    owner_id: "aws_sdk_codeconnections.types.owner_id.OwnerId"
    """<p>The owner ID for a specific revision, such as the GitHub owner ID for a GitHub repository.</p>"""
    repository_name: "aws_sdk_codeconnections.types.repository_name.RepositoryName"
    """<p>The repository name for a specific revision.</p>"""
    provider_type: "aws_sdk_codeconnections.types.provider_type.ProviderType"
    """<p>The provider type for a revision, such as GitHub.</p>"""
    sha: "aws_sdk_codeconnections.types.sha.SHA"
    """<p>The SHA, such as the commit ID, for a specific revision.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Revision) -> dict:
    out: dict = {}
    out["Branch"] = value["branch"]
    out["Directory"] = value["directory"]
    out["OwnerId"] = value["owner_id"]
    out["RepositoryName"] = value["repository_name"]
    import aws_sdk_codeconnections.types.provider_type

    out["ProviderType"] = (
        aws_sdk_codeconnections.types.provider_type.serialize_aws_json_1_0(
            value["provider_type"]
        )
    )
    out["Sha"] = value["sha"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Revision:
    out: Revision = {}  # type: ignore[typeddict-item]
    if "Branch" in data:
        out["branch"] = data["Branch"]
    else:
        raise DeserializationError("Revision.branch required")
    if "Directory" in data:
        out["directory"] = data["Directory"]
    else:
        raise DeserializationError("Revision.directory required")
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    else:
        raise DeserializationError("Revision.owner_id required")
    if "RepositoryName" in data:
        out["repository_name"] = data["RepositoryName"]
    else:
        raise DeserializationError("Revision.repository_name required")
    if "ProviderType" in data:
        import aws_sdk_codeconnections.types.provider_type

        out["provider_type"] = (
            aws_sdk_codeconnections.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderType"]
            )
        )
    else:
        raise DeserializationError("Revision.provider_type required")
    if "Sha" in data:
        out["sha"] = data["Sha"]
    else:
        raise DeserializationError("Revision.sha required")
    return out
