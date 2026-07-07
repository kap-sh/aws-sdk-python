"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#Property``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.eo_cloud_cover_input
    import aws_sdk_sagemaker_geospatial.types.landsat_cloud_cover_land_input
    import aws_sdk_sagemaker_geospatial.types.platform_input
    import aws_sdk_sagemaker_geospatial.types.view_off_nadir_input
    import aws_sdk_sagemaker_geospatial.types.view_sun_azimuth_input
    import aws_sdk_sagemaker_geospatial.types.view_sun_elevation_input


class _Property_EoCloudCover(TypedDict, closed=True):
    EoCloudCover: (
        "aws_sdk_sagemaker_geospatial.types.eo_cloud_cover_input.EoCloudCoverInput"
    )


class _Property_ViewOffNadir(TypedDict, closed=True):
    ViewOffNadir: (
        "aws_sdk_sagemaker_geospatial.types.view_off_nadir_input.ViewOffNadirInput"
    )


class _Property_ViewSunAzimuth(TypedDict, closed=True):
    ViewSunAzimuth: (
        "aws_sdk_sagemaker_geospatial.types.view_sun_azimuth_input.ViewSunAzimuthInput"
    )


class _Property_ViewSunElevation(TypedDict, closed=True):
    ViewSunElevation: "aws_sdk_sagemaker_geospatial.types.view_sun_elevation_input.ViewSunElevationInput"


class _Property_Platform(TypedDict, closed=True):
    Platform: "aws_sdk_sagemaker_geospatial.types.platform_input.PlatformInput"


class _Property_LandsatCloudCoverLand(TypedDict, closed=True):
    LandsatCloudCoverLand: "aws_sdk_sagemaker_geospatial.types.landsat_cloud_cover_land_input.LandsatCloudCoverLandInput"


Property: TypeAlias = (
    _Property_EoCloudCover
    | _Property_ViewOffNadir
    | _Property_ViewSunAzimuth
    | _Property_ViewSunElevation
    | _Property_Platform
    | _Property_LandsatCloudCoverLand
)


# --- restJson1 ser/de ---
def serialize_json(value: Property) -> dict:
    if "EoCloudCover" in value:
        import aws_sdk_sagemaker_geospatial.types.eo_cloud_cover_input

        return {
            "EoCloudCover": aws_sdk_sagemaker_geospatial.types.eo_cloud_cover_input.serialize_json(
                value["EoCloudCover"]
            )
        }
    elif "ViewOffNadir" in value:
        import aws_sdk_sagemaker_geospatial.types.view_off_nadir_input

        return {
            "ViewOffNadir": aws_sdk_sagemaker_geospatial.types.view_off_nadir_input.serialize_json(
                value["ViewOffNadir"]
            )
        }
    elif "ViewSunAzimuth" in value:
        import aws_sdk_sagemaker_geospatial.types.view_sun_azimuth_input

        return {
            "ViewSunAzimuth": aws_sdk_sagemaker_geospatial.types.view_sun_azimuth_input.serialize_json(
                value["ViewSunAzimuth"]
            )
        }
    elif "ViewSunElevation" in value:
        import aws_sdk_sagemaker_geospatial.types.view_sun_elevation_input

        return {
            "ViewSunElevation": aws_sdk_sagemaker_geospatial.types.view_sun_elevation_input.serialize_json(
                value["ViewSunElevation"]
            )
        }
    elif "Platform" in value:
        import aws_sdk_sagemaker_geospatial.types.platform_input

        return {
            "Platform": aws_sdk_sagemaker_geospatial.types.platform_input.serialize_json(
                value["Platform"]
            )
        }
    elif "LandsatCloudCoverLand" in value:
        import aws_sdk_sagemaker_geospatial.types.landsat_cloud_cover_land_input

        return {
            "LandsatCloudCoverLand": aws_sdk_sagemaker_geospatial.types.landsat_cloud_cover_land_input.serialize_json(
                value["LandsatCloudCoverLand"]
            )
        }
    else:
        raise SerializationError("Property: no variant present")


def deserialize_json(data: dict) -> Property:
    if "EoCloudCover" in data:
        import aws_sdk_sagemaker_geospatial.types.eo_cloud_cover_input

        return {
            "EoCloudCover": aws_sdk_sagemaker_geospatial.types.eo_cloud_cover_input.deserialize_json(
                data["EoCloudCover"]
            )
        }
    elif "ViewOffNadir" in data:
        import aws_sdk_sagemaker_geospatial.types.view_off_nadir_input

        return {
            "ViewOffNadir": aws_sdk_sagemaker_geospatial.types.view_off_nadir_input.deserialize_json(
                data["ViewOffNadir"]
            )
        }
    elif "ViewSunAzimuth" in data:
        import aws_sdk_sagemaker_geospatial.types.view_sun_azimuth_input

        return {
            "ViewSunAzimuth": aws_sdk_sagemaker_geospatial.types.view_sun_azimuth_input.deserialize_json(
                data["ViewSunAzimuth"]
            )
        }
    elif "ViewSunElevation" in data:
        import aws_sdk_sagemaker_geospatial.types.view_sun_elevation_input

        return {
            "ViewSunElevation": aws_sdk_sagemaker_geospatial.types.view_sun_elevation_input.deserialize_json(
                data["ViewSunElevation"]
            )
        }
    elif "Platform" in data:
        import aws_sdk_sagemaker_geospatial.types.platform_input

        return {
            "Platform": aws_sdk_sagemaker_geospatial.types.platform_input.deserialize_json(
                data["Platform"]
            )
        }
    elif "LandsatCloudCoverLand" in data:
        import aws_sdk_sagemaker_geospatial.types.landsat_cloud_cover_land_input

        return {
            "LandsatCloudCoverLand": aws_sdk_sagemaker_geospatial.types.landsat_cloud_cover_land_input.deserialize_json(
                data["LandsatCloudCoverLand"]
            )
        }
    else:
        raise DeserializationError("Property: no recognized variant key")
