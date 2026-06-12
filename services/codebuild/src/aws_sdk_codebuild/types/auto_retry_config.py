"""Generated from Smithy shape ``com.amazonaws.codebuild#AutoRetryConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.string
    import aws_sdk_codebuild.types.wrapper_int


class AutoRetryConfig(TypedDict):
    auto_retry_limit: NotRequired["aws_sdk_codebuild.types.wrapper_int.WrapperInt"]
    """<p>The maximum number of additional automatic retries after a failed build. For example, if the auto-retry limit is set to 2, CodeBuild will call the <code>RetryBuild</code> API to automatically retry your build for up to 2 additional times.</p>"""
    auto_retry_number: NotRequired["aws_sdk_codebuild.types.wrapper_int.WrapperInt"]
    """<p>The number of times that the build has been retried. The initial build will have an auto-retry number of 0.</p>"""
    next_auto_retry: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The build ARN of the auto-retried build triggered by the current build. The next auto-retry will be <code>null</code> for builds that don't trigger an auto-retry.</p>"""
    previous_auto_retry: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The build ARN of the build that triggered the current auto-retry build. The previous auto-retry will be <code>null</code> for the initial build.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoRetryConfig) -> dict:
    out: dict = {}
    if "auto_retry_limit" in value:
        out["autoRetryLimit"] = value["auto_retry_limit"]
    if "auto_retry_number" in value:
        out["autoRetryNumber"] = value["auto_retry_number"]
    if "next_auto_retry" in value:
        out["nextAutoRetry"] = value["next_auto_retry"]
    if "previous_auto_retry" in value:
        out["previousAutoRetry"] = value["previous_auto_retry"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoRetryConfig:
    out: AutoRetryConfig = {}  # type: ignore[typeddict-item]
    if "autoRetryLimit" in data:
        out["auto_retry_limit"] = data["autoRetryLimit"]
    if "autoRetryNumber" in data:
        out["auto_retry_number"] = data["autoRetryNumber"]
    if "nextAutoRetry" in data:
        out["next_auto_retry"] = data["nextAutoRetry"]
    if "previousAutoRetry" in data:
        out["previous_auto_retry"] = data["previousAutoRetry"]
    return out
