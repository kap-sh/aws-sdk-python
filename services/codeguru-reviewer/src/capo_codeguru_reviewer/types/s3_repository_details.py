"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#S3RepositoryDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.code_artifacts
    import capo_codeguru_reviewer.types.s3_bucket_name


class S3RepositoryDetails(TypedDict, closed=True):
    bucket_name: NotRequired["capo_codeguru_reviewer.types.s3_bucket_name.S3BucketName"]
    """<p>The name of the S3 bucket used for associating a new S3 repository. It must begin with <code>codeguru-reviewer-</code>. </p>"""
    code_artifacts: NotRequired[
        "capo_codeguru_reviewer.types.code_artifacts.CodeArtifacts"
    ]
    """<p>A <code>CodeArtifacts</code> object. The <code>CodeArtifacts</code> object includes the S3 object key for a source code .zip file and for a build artifacts .zip file that contains .jar or .class files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3RepositoryDetails) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["BucketName"] = value["bucket_name"]
    if "code_artifacts" in value:
        import capo_codeguru_reviewer.types.code_artifacts

        out["CodeArtifacts"] = (
            capo_codeguru_reviewer.types.code_artifacts.serialize_json(
                value["code_artifacts"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3RepositoryDetails:
    out: S3RepositoryDetails = {}  # type: ignore[typeddict-item]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    if "CodeArtifacts" in data:
        import capo_codeguru_reviewer.types.code_artifacts

        out["code_artifacts"] = (
            capo_codeguru_reviewer.types.code_artifacts.deserialize_json(
                data["CodeArtifacts"]
            )
        )
    return out
