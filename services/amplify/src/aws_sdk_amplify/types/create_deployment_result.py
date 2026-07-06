"""Generated from Smithy shape ``com.amazonaws.amplify#CreateDeploymentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.file_upload_urls
    import aws_sdk_amplify.types.job_id
    import aws_sdk_amplify.types.upload_url


class CreateDeploymentResult(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_amplify.types.job_id.JobId"]
    """<p> The job ID for this deployment. will supply to start deployment api. </p>"""
    file_upload_urls: "aws_sdk_amplify.types.file_upload_urls.FileUploadUrls"
    """<p> When the <code>fileMap</code> argument is provided in the request, <code>fileUploadUrls</code> will contain a map of file names to upload URLs. </p>"""
    zip_upload_url: "aws_sdk_amplify.types.upload_url.UploadUrl"
    """<p> When the <code>fileMap</code> argument is not provided in the request, this <code>zipUploadUrl</code> is returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeploymentResult) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    import aws_sdk_amplify.types.file_upload_urls

    out["fileUploadUrls"] = aws_sdk_amplify.types.file_upload_urls.serialize_json(
        value["file_upload_urls"]
    )
    out["zipUploadUrl"] = value["zip_upload_url"]
    return out


def deserialize_json(data: dict) -> CreateDeploymentResult:
    out: CreateDeploymentResult = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "fileUploadUrls" in data:
        import aws_sdk_amplify.types.file_upload_urls

        out["file_upload_urls"] = (
            aws_sdk_amplify.types.file_upload_urls.deserialize_json(
                data["fileUploadUrls"]
            )
        )
    else:
        raise DeserializationError("CreateDeploymentResult.file_upload_urls required")
    if "zipUploadUrl" in data:
        out["zip_upload_url"] = data["zipUploadUrl"]
    else:
        raise DeserializationError("CreateDeploymentResult.zip_upload_url required")
    return out
