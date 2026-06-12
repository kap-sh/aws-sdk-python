"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#LocalSizeConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.max_local_media_size_in_mb
    import aws_sdk_kinesis_video.types.strategy_on_full_size


class LocalSizeConfig(TypedDict):
    max_local_media_size_in_mb: NotRequired[
        "aws_sdk_kinesis_video.types.max_local_media_size_in_mb.MaxLocalMediaSizeInMB"
    ]
    """<p>The overall maximum size of the media that you want to store for a stream on the Edge Agent. </p>"""
    strategy_on_full_size: NotRequired[
        "aws_sdk_kinesis_video.types.strategy_on_full_size.StrategyOnFullSize"
    ]
    """<p>The strategy to perform when a stream’s <code>MaxLocalMediaSizeInMB</code> limit is reached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LocalSizeConfig) -> dict:
    out: dict = {}
    if "max_local_media_size_in_mb" in value:
        out["MaxLocalMediaSizeInMB"] = value["max_local_media_size_in_mb"]
    if "strategy_on_full_size" in value:
        import aws_sdk_kinesis_video.types.strategy_on_full_size

        out["StrategyOnFullSize"] = (
            aws_sdk_kinesis_video.types.strategy_on_full_size.serialize_json(
                value["strategy_on_full_size"]
            )
        )
    return out


def deserialize_json(data: dict) -> LocalSizeConfig:
    out: LocalSizeConfig = {}  # type: ignore[typeddict-item]
    if "MaxLocalMediaSizeInMB" in data:
        out["max_local_media_size_in_mb"] = data["MaxLocalMediaSizeInMB"]
    if "StrategyOnFullSize" in data:
        import aws_sdk_kinesis_video.types.strategy_on_full_size

        out["strategy_on_full_size"] = (
            aws_sdk_kinesis_video.types.strategy_on_full_size.deserialize_json(
                data["StrategyOnFullSize"]
            )
        )
    return out
