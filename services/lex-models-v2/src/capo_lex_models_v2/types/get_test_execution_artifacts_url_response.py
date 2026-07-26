"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#GetTestExecutionArtifactsUrlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.presigned_s3_url


class GetTestExecutionArtifactsUrlResponse(TypedDict, closed=True):
    test_execution_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the completed test execution.</p>"""
    download_artifacts_url: NotRequired[
        "capo_lex_models_v2.types.presigned_s3_url.PresignedS3Url"
    ]
    """<p>The pre-signed Amazon S3 URL to download completed test execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTestExecutionArtifactsUrlResponse) -> dict:
    out: dict = {}
    if "test_execution_id" in value:
        out["testExecutionId"] = value["test_execution_id"]
    if "download_artifacts_url" in value:
        out["downloadArtifactsUrl"] = value["download_artifacts_url"]
    return out


def deserialize_json(data: dict) -> GetTestExecutionArtifactsUrlResponse:
    out: GetTestExecutionArtifactsUrlResponse = {}  # type: ignore[typeddict-item]
    if "testExecutionId" in data:
        out["test_execution_id"] = data["testExecutionId"]
    if "downloadArtifactsUrl" in data:
        out["download_artifacts_url"] = data["downloadArtifactsUrl"]
    return out
