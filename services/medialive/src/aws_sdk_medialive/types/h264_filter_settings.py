"""Generated from Smithy shape ``com.amazonaws.medialive#H264FilterSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.bandwidth_reduction_filter_settings
    import aws_sdk_medialive.types.temporal_filter_settings


class H264FilterSettings(TypedDict):
    temporal_filter_settings: NotRequired[
        "aws_sdk_medialive.types.temporal_filter_settings.TemporalFilterSettings"
    ]
    bandwidth_reduction_filter_settings: NotRequired[
        "aws_sdk_medialive.types.bandwidth_reduction_filter_settings.BandwidthReductionFilterSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: H264FilterSettings) -> dict:
    out: dict = {}
    if "temporal_filter_settings" in value:
        import aws_sdk_medialive.types.temporal_filter_settings

        out["temporalFilterSettings"] = (
            aws_sdk_medialive.types.temporal_filter_settings.serialize_json(
                value["temporal_filter_settings"]
            )
        )
    if "bandwidth_reduction_filter_settings" in value:
        import aws_sdk_medialive.types.bandwidth_reduction_filter_settings

        out["bandwidthReductionFilterSettings"] = (
            aws_sdk_medialive.types.bandwidth_reduction_filter_settings.serialize_json(
                value["bandwidth_reduction_filter_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> H264FilterSettings:
    out: H264FilterSettings = {}  # type: ignore[typeddict-item]
    if "temporalFilterSettings" in data:
        import aws_sdk_medialive.types.temporal_filter_settings

        out["temporal_filter_settings"] = (
            aws_sdk_medialive.types.temporal_filter_settings.deserialize_json(
                data["temporalFilterSettings"]
            )
        )
    if "bandwidthReductionFilterSettings" in data:
        import aws_sdk_medialive.types.bandwidth_reduction_filter_settings

        out["bandwidth_reduction_filter_settings"] = (
            aws_sdk_medialive.types.bandwidth_reduction_filter_settings.deserialize_json(
                data["bandwidthReductionFilterSettings"]
            )
        )
    return out
