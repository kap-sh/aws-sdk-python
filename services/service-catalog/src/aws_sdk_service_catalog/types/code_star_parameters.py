"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CodeStarParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.code_star_connection_arn
    import aws_sdk_service_catalog.types.repository
    import aws_sdk_service_catalog.types.repository_artifact_path
    import aws_sdk_service_catalog.types.repository_branch


class CodeStarParameters(TypedDict, closed=True):
    connection_arn: (
        "aws_sdk_service_catalog.types.code_star_connection_arn.CodeStarConnectionArn"
    )
    """<p>The CodeStar ARN, which is the connection between Service Catalog and the external repository.</p>"""
    repository: "aws_sdk_service_catalog.types.repository.Repository"
    r"""<p>The specific repository where the product’s artifact-to-be-synced resides, formatted as \"Account/Repo.\" </p>"""
    branch: "aws_sdk_service_catalog.types.repository_branch.RepositoryBranch"
    """<p>The specific branch where the artifact resides. </p>"""
    artifact_path: (
        "aws_sdk_service_catalog.types.repository_artifact_path.RepositoryArtifactPath"
    )
    r"""<p>The absolute path wehre the artifact resides within the repo and branch, formatted as \"folder/file.json.\" </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeStarParameters) -> dict:
    out: dict = {}
    out["ConnectionArn"] = value["connection_arn"]
    out["Repository"] = value["repository"]
    out["Branch"] = value["branch"]
    out["ArtifactPath"] = value["artifact_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeStarParameters:
    out: CodeStarParameters = {}  # type: ignore[typeddict-item]
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    else:
        raise DeserializationError("CodeStarParameters.connection_arn required")
    if "Repository" in data:
        out["repository"] = data["Repository"]
    else:
        raise DeserializationError("CodeStarParameters.repository required")
    if "Branch" in data:
        out["branch"] = data["Branch"]
    else:
        raise DeserializationError("CodeStarParameters.branch required")
    if "ArtifactPath" in data:
        out["artifact_path"] = data["ArtifactPath"]
    else:
        raise DeserializationError("CodeStarParameters.artifact_path required")
    return out
