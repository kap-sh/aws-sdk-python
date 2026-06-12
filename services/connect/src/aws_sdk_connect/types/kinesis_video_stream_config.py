"""Generated from Smithy shape ``com.amazonaws.connect#KinesisVideoStreamConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.encryption_config
    import aws_sdk_connect.types.hours
    import aws_sdk_connect.types.prefix


class KinesisVideoStreamConfig(TypedDict):
    prefix: "aws_sdk_connect.types.prefix.Prefix"
    """<p>The prefix of the video stream.</p>"""
    retention_period_hours: "aws_sdk_connect.types.hours.Hours"
    """<p>The number of hours data is retained in the stream. Kinesis Video Streams retains the data in a data store that is associated with the stream.</p> <p>The default value is 0, indicating that the stream does not persist data.</p>"""
    encryption_config: "aws_sdk_connect.types.encryption_config.EncryptionConfig"
    """<p>The encryption configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisVideoStreamConfig) -> dict:
    out: dict = {}
    out["Prefix"] = value["prefix"]
    out["RetentionPeriodHours"] = value.get("retention_period_hours", 0)
    import aws_sdk_connect.types.encryption_config

    out["EncryptionConfig"] = aws_sdk_connect.types.encryption_config.serialize_json(
        value["encryption_config"]
    )
    return out


def deserialize_json(data: dict) -> KinesisVideoStreamConfig:
    out: KinesisVideoStreamConfig = {}  # type: ignore[typeddict-item]
    if "Prefix" in data:
        out["prefix"] = data["Prefix"]
    else:
        raise DeserializationError("KinesisVideoStreamConfig.prefix required")
    if "RetentionPeriodHours" in data:
        out["retention_period_hours"] = data["RetentionPeriodHours"]
    else:
        out["retention_period_hours"] = 0
    if "EncryptionConfig" in data:
        import aws_sdk_connect.types.encryption_config

        out["encryption_config"] = (
            aws_sdk_connect.types.encryption_config.deserialize_json(
                data["EncryptionConfig"]
            )
        )
    else:
        raise DeserializationError(
            "KinesisVideoStreamConfig.encryption_config required"
        )
    return out
