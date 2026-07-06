"""Generated from Smithy shape ``com.amazonaws.ssm#SessionManagerOutputUrl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.session_manager_cloud_watch_output_url
    import aws_sdk_ssm.types.session_manager_s3_output_url


class SessionManagerOutputUrl(TypedDict, closed=True):
    s3_output_url: NotRequired[
        "aws_sdk_ssm.types.session_manager_s3_output_url.SessionManagerS3OutputUrl"
    ]
    """<p>Reserved for future use.</p>"""
    cloud_watch_output_url: NotRequired[
        "aws_sdk_ssm.types.session_manager_cloud_watch_output_url.SessionManagerCloudWatchOutputUrl"
    ]
    """<p>Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionManagerOutputUrl) -> dict:
    out: dict = {}
    if "s3_output_url" in value:
        out["S3OutputUrl"] = value["s3_output_url"]
    if "cloud_watch_output_url" in value:
        out["CloudWatchOutputUrl"] = value["cloud_watch_output_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionManagerOutputUrl:
    out: SessionManagerOutputUrl = {}  # type: ignore[typeddict-item]
    if "S3OutputUrl" in data:
        out["s3_output_url"] = data["S3OutputUrl"]
    if "CloudWatchOutputUrl" in data:
        out["cloud_watch_output_url"] = data["CloudWatchOutputUrl"]
    return out
