"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#LocalSizeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.max_local_media_size_in_mb
    import capo_kinesis_video.types.strategy_on_full_size


class LocalSizeConfig(TypedDict, closed=True):
    max_local_media_size_in_mb: NotRequired[
        "capo_kinesis_video.types.max_local_media_size_in_mb.MaxLocalMediaSizeInMB"
    ]
    """<p>The overall maximum size of the media that you want to store for a stream on the Edge Agent. </p>"""
    strategy_on_full_size: NotRequired[
        "capo_kinesis_video.types.strategy_on_full_size.StrategyOnFullSize"
    ]
    """<p>The strategy to perform when a stream’s <code>MaxLocalMediaSizeInMB</code> limit is reached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LocalSizeConfig) -> dict:
    out: dict = {}
    if "max_local_media_size_in_mb" in value:
        out["MaxLocalMediaSizeInMB"] = value["max_local_media_size_in_mb"]
    if "strategy_on_full_size" in value:
        import capo_kinesis_video.types.strategy_on_full_size

        out["StrategyOnFullSize"] = (
            capo_kinesis_video.types.strategy_on_full_size.serialize_json(
                value["strategy_on_full_size"]
            )
        )
    return out


def deserialize_json(data: dict) -> LocalSizeConfig:
    out: LocalSizeConfig = {}  # type: ignore[typeddict-item]
    if "MaxLocalMediaSizeInMB" in data:
        out["max_local_media_size_in_mb"] = data["MaxLocalMediaSizeInMB"]
    if "StrategyOnFullSize" in data:
        import capo_kinesis_video.types.strategy_on_full_size

        out["strategy_on_full_size"] = (
            capo_kinesis_video.types.strategy_on_full_size.deserialize_json(
                data["StrategyOnFullSize"]
            )
        )
    return out
