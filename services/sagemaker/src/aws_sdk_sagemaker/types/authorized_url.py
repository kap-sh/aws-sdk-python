"""Generated from Smithy shape ``com.amazonaws.sagemaker#AuthorizedUrl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.local_path
    import aws_sdk_sagemaker.types.long_s3_uri


class AuthorizedUrl(TypedDict, closed=True):
    url: NotRequired["aws_sdk_sagemaker.types.long_s3_uri.LongS3Uri"]
    """<p>The presigned S3 URL that provides temporary, secure access to download the file. URLs expire within 15 minutes for security purposes.</p>"""
    local_path: NotRequired["aws_sdk_sagemaker.types.local_path.LocalPath"]
    """<p>The recommended local file path where the downloaded file should be stored to maintain proper directory structure and file organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthorizedUrl) -> dict:
    out: dict = {}
    if "url" in value:
        out["Url"] = value["url"]
    if "local_path" in value:
        out["LocalPath"] = value["local_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthorizedUrl:
    out: AuthorizedUrl = {}  # type: ignore[typeddict-item]
    if "Url" in data:
        out["url"] = data["Url"]
    if "LocalPath" in data:
        out["local_path"] = data["LocalPath"]
    return out
