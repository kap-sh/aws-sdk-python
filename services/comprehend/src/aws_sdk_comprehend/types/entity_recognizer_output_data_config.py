"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerOutputDataConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.s3_uri


class EntityRecognizerOutputDataConfig(TypedDict):
    flywheel_stats_s3_prefix: NotRequired["aws_sdk_comprehend.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 prefix for the data lake location of the flywheel statistics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerOutputDataConfig) -> dict:
    out: dict = {}
    if "flywheel_stats_s3_prefix" in value:
        out["FlywheelStatsS3Prefix"] = value["flywheel_stats_s3_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityRecognizerOutputDataConfig:
    out: EntityRecognizerOutputDataConfig = {}  # type: ignore[typeddict-item]
    if "FlywheelStatsS3Prefix" in data:
        out["flywheel_stats_s3_prefix"] = data["FlywheelStatsS3Prefix"]
    return out
