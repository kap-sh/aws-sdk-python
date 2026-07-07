"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringConstraintsResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.s3_uri


class MonitoringConstraintsResource(TypedDict, closed=True):
    s3_uri: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 URI for the constraints resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringConstraintsResource) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringConstraintsResource:
    out: MonitoringConstraintsResource = {}  # type: ignore[typeddict-item]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    return out
