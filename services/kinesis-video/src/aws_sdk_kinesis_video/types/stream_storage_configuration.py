"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#StreamStorageConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.default_storage_tier


class StreamStorageConfiguration(TypedDict):
    default_storage_tier: (
        "aws_sdk_kinesis_video.types.default_storage_tier.DefaultStorageTier"
    )
    """<p>The default storage tier for the stream data. This setting determines the storage class used for stream data, affecting both performance characteristics and storage costs.</p> <p>Available storage tiers:</p> <ul> <li> <p> <code>HOT</code> - Optimized for frequent access with the lowest latency and highest performance. Ideal for real-time applications and frequently accessed data.</p> </li> <li> <p> <code>WARM</code> - Balanced performance and cost for moderately accessed data. Suitable for data that is accessed regularly but not continuously.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamStorageConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_video.types.default_storage_tier

    out["DefaultStorageTier"] = (
        aws_sdk_kinesis_video.types.default_storage_tier.serialize_json(
            value["default_storage_tier"]
        )
    )
    return out


def deserialize_json(data: dict) -> StreamStorageConfiguration:
    out: StreamStorageConfiguration = {}  # type: ignore[typeddict-item]
    if "DefaultStorageTier" in data:
        import aws_sdk_kinesis_video.types.default_storage_tier

        out["default_storage_tier"] = (
            aws_sdk_kinesis_video.types.default_storage_tier.deserialize_json(
                data["DefaultStorageTier"]
            )
        )
    else:
        raise DeserializationError(
            "StreamStorageConfiguration.default_storage_tier required"
        )
    return out
