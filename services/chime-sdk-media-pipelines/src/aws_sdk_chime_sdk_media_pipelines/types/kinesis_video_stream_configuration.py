"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#KinesisVideoStreamConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.aws_region
    import aws_sdk_chime_sdk_media_pipelines.types.data_retention_in_hours


class KinesisVideoStreamConfiguration(TypedDict):
    region: "aws_sdk_chime_sdk_media_pipelines.types.aws_region.AwsRegion"
    """<p>The Amazon Web Services Region of the video stream.</p>"""
    data_retention_in_hours: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.data_retention_in_hours.DataRetentionInHours"
    ]
    """<p>The amount of time that data is retained.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisVideoStreamConfiguration) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    if "data_retention_in_hours" in value:
        out["DataRetentionInHours"] = value["data_retention_in_hours"]
    return out


def deserialize_json(data: dict) -> KinesisVideoStreamConfiguration:
    out: KinesisVideoStreamConfiguration = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    else:
        raise DeserializationError("KinesisVideoStreamConfiguration.region required")
    if "DataRetentionInHours" in data:
        out["data_retention_in_hours"] = data["DataRetentionInHours"]
    return out
