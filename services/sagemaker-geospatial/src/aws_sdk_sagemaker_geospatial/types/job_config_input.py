"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#JobConfigInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.band_math_config_input
    import aws_sdk_sagemaker_geospatial.types.cloud_masking_config_input
    import aws_sdk_sagemaker_geospatial.types.cloud_removal_config_input
    import aws_sdk_sagemaker_geospatial.types.geo_mosaic_config_input
    import aws_sdk_sagemaker_geospatial.types.land_cover_segmentation_config_input
    import aws_sdk_sagemaker_geospatial.types.resampling_config_input
    import aws_sdk_sagemaker_geospatial.types.stack_config_input
    import aws_sdk_sagemaker_geospatial.types.temporal_statistics_config_input
    import aws_sdk_sagemaker_geospatial.types.zonal_statistics_config_input


class _JobConfigInput_BandMathConfig(TypedDict, closed=True):
    BandMathConfig: (
        "aws_sdk_sagemaker_geospatial.types.band_math_config_input.BandMathConfigInput"
    )


class _JobConfigInput_ResamplingConfig(TypedDict, closed=True):
    ResamplingConfig: "aws_sdk_sagemaker_geospatial.types.resampling_config_input.ResamplingConfigInput"


class _JobConfigInput_TemporalStatisticsConfig(TypedDict, closed=True):
    TemporalStatisticsConfig: "aws_sdk_sagemaker_geospatial.types.temporal_statistics_config_input.TemporalStatisticsConfigInput"


class _JobConfigInput_CloudRemovalConfig(TypedDict, closed=True):
    CloudRemovalConfig: "aws_sdk_sagemaker_geospatial.types.cloud_removal_config_input.CloudRemovalConfigInput"


class _JobConfigInput_ZonalStatisticsConfig(TypedDict, closed=True):
    ZonalStatisticsConfig: "aws_sdk_sagemaker_geospatial.types.zonal_statistics_config_input.ZonalStatisticsConfigInput"


class _JobConfigInput_GeoMosaicConfig(TypedDict, closed=True):
    GeoMosaicConfig: "aws_sdk_sagemaker_geospatial.types.geo_mosaic_config_input.GeoMosaicConfigInput"


class _JobConfigInput_StackConfig(TypedDict, closed=True):
    StackConfig: (
        "aws_sdk_sagemaker_geospatial.types.stack_config_input.StackConfigInput"
    )


class _JobConfigInput_CloudMaskingConfig(TypedDict, closed=True):
    CloudMaskingConfig: "aws_sdk_sagemaker_geospatial.types.cloud_masking_config_input.CloudMaskingConfigInput"


class _JobConfigInput_LandCoverSegmentationConfig(TypedDict, closed=True):
    LandCoverSegmentationConfig: "aws_sdk_sagemaker_geospatial.types.land_cover_segmentation_config_input.LandCoverSegmentationConfigInput"


JobConfigInput: TypeAlias = (
    _JobConfigInput_BandMathConfig
    | _JobConfigInput_ResamplingConfig
    | _JobConfigInput_TemporalStatisticsConfig
    | _JobConfigInput_CloudRemovalConfig
    | _JobConfigInput_ZonalStatisticsConfig
    | _JobConfigInput_GeoMosaicConfig
    | _JobConfigInput_StackConfig
    | _JobConfigInput_CloudMaskingConfig
    | _JobConfigInput_LandCoverSegmentationConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: JobConfigInput) -> dict:
    if "BandMathConfig" in value:
        import aws_sdk_sagemaker_geospatial.types.band_math_config_input

        return {
            "BandMathConfig": aws_sdk_sagemaker_geospatial.types.band_math_config_input.serialize_json(
                value["BandMathConfig"]
            )
        }
    elif "ResamplingConfig" in value:
        import aws_sdk_sagemaker_geospatial.types.resampling_config_input

        return {
            "ResamplingConfig": aws_sdk_sagemaker_geospatial.types.resampling_config_input.serialize_json(
                value["ResamplingConfig"]
            )
        }
    elif "TemporalStatisticsConfig" in value:
        import aws_sdk_sagemaker_geospatial.types.temporal_statistics_config_input

        return {
            "TemporalStatisticsConfig": aws_sdk_sagemaker_geospatial.types.temporal_statistics_config_input.serialize_json(
                value["TemporalStatisticsConfig"]
            )
        }
    elif "CloudRemovalConfig" in value:
        import aws_sdk_sagemaker_geospatial.types.cloud_removal_config_input

        return {
            "CloudRemovalConfig": aws_sdk_sagemaker_geospatial.types.cloud_removal_config_input.serialize_json(
                value["CloudRemovalConfig"]
            )
        }
    elif "ZonalStatisticsConfig" in value:
        import aws_sdk_sagemaker_geospatial.types.zonal_statistics_config_input

        return {
            "ZonalStatisticsConfig": aws_sdk_sagemaker_geospatial.types.zonal_statistics_config_input.serialize_json(
                value["ZonalStatisticsConfig"]
            )
        }
    elif "GeoMosaicConfig" in value:
        import aws_sdk_sagemaker_geospatial.types.geo_mosaic_config_input

        return {
            "GeoMosaicConfig": aws_sdk_sagemaker_geospatial.types.geo_mosaic_config_input.serialize_json(
                value["GeoMosaicConfig"]
            )
        }
    elif "StackConfig" in value:
        import aws_sdk_sagemaker_geospatial.types.stack_config_input

        return {
            "StackConfig": aws_sdk_sagemaker_geospatial.types.stack_config_input.serialize_json(
                value["StackConfig"]
            )
        }
    elif "CloudMaskingConfig" in value:
        import aws_sdk_sagemaker_geospatial.types.cloud_masking_config_input

        return {
            "CloudMaskingConfig": aws_sdk_sagemaker_geospatial.types.cloud_masking_config_input.serialize_json(
                value["CloudMaskingConfig"]
            )
        }
    elif "LandCoverSegmentationConfig" in value:
        import aws_sdk_sagemaker_geospatial.types.land_cover_segmentation_config_input

        return {
            "LandCoverSegmentationConfig": aws_sdk_sagemaker_geospatial.types.land_cover_segmentation_config_input.serialize_json(
                value["LandCoverSegmentationConfig"]
            )
        }
    else:
        raise SerializationError("JobConfigInput: no variant present")


def deserialize_json(data: dict) -> JobConfigInput:
    if "BandMathConfig" in data:
        import aws_sdk_sagemaker_geospatial.types.band_math_config_input

        return {
            "BandMathConfig": aws_sdk_sagemaker_geospatial.types.band_math_config_input.deserialize_json(
                data["BandMathConfig"]
            )
        }
    elif "ResamplingConfig" in data:
        import aws_sdk_sagemaker_geospatial.types.resampling_config_input

        return {
            "ResamplingConfig": aws_sdk_sagemaker_geospatial.types.resampling_config_input.deserialize_json(
                data["ResamplingConfig"]
            )
        }
    elif "TemporalStatisticsConfig" in data:
        import aws_sdk_sagemaker_geospatial.types.temporal_statistics_config_input

        return {
            "TemporalStatisticsConfig": aws_sdk_sagemaker_geospatial.types.temporal_statistics_config_input.deserialize_json(
                data["TemporalStatisticsConfig"]
            )
        }
    elif "CloudRemovalConfig" in data:
        import aws_sdk_sagemaker_geospatial.types.cloud_removal_config_input

        return {
            "CloudRemovalConfig": aws_sdk_sagemaker_geospatial.types.cloud_removal_config_input.deserialize_json(
                data["CloudRemovalConfig"]
            )
        }
    elif "ZonalStatisticsConfig" in data:
        import aws_sdk_sagemaker_geospatial.types.zonal_statistics_config_input

        return {
            "ZonalStatisticsConfig": aws_sdk_sagemaker_geospatial.types.zonal_statistics_config_input.deserialize_json(
                data["ZonalStatisticsConfig"]
            )
        }
    elif "GeoMosaicConfig" in data:
        import aws_sdk_sagemaker_geospatial.types.geo_mosaic_config_input

        return {
            "GeoMosaicConfig": aws_sdk_sagemaker_geospatial.types.geo_mosaic_config_input.deserialize_json(
                data["GeoMosaicConfig"]
            )
        }
    elif "StackConfig" in data:
        import aws_sdk_sagemaker_geospatial.types.stack_config_input

        return {
            "StackConfig": aws_sdk_sagemaker_geospatial.types.stack_config_input.deserialize_json(
                data["StackConfig"]
            )
        }
    elif "CloudMaskingConfig" in data:
        import aws_sdk_sagemaker_geospatial.types.cloud_masking_config_input

        return {
            "CloudMaskingConfig": aws_sdk_sagemaker_geospatial.types.cloud_masking_config_input.deserialize_json(
                data["CloudMaskingConfig"]
            )
        }
    elif "LandCoverSegmentationConfig" in data:
        import aws_sdk_sagemaker_geospatial.types.land_cover_segmentation_config_input

        return {
            "LandCoverSegmentationConfig": aws_sdk_sagemaker_geospatial.types.land_cover_segmentation_config_input.deserialize_json(
                data["LandCoverSegmentationConfig"]
            )
        }
    else:
        raise DeserializationError("JobConfigInput: no recognized variant key")
