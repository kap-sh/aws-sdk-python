"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#KinesisVideoStreamConfigurationUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.data_retention_change_in_hours


class KinesisVideoStreamConfigurationUpdate(TypedDict):
    data_retention_in_hours: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.data_retention_change_in_hours.DataRetentionChangeInHours"
    ]
    """<p>The updated time that data is retained.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisVideoStreamConfigurationUpdate) -> dict:
    out: dict = {}
    if "data_retention_in_hours" in value:
        out["DataRetentionInHours"] = value["data_retention_in_hours"]
    return out


def deserialize_json(data: dict) -> KinesisVideoStreamConfigurationUpdate:
    out: KinesisVideoStreamConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "DataRetentionInHours" in data:
        out["data_retention_in_hours"] = data["DataRetentionInHours"]
    return out
