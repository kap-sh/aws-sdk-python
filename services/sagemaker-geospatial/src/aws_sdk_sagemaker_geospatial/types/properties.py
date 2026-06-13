"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#Properties``."""

from typing import TypedDict

from typing_extensions import NotRequired


class Properties(TypedDict):
    eo_cloud_cover: NotRequired["float"]
    """<p>Estimate of cloud cover.</p>"""
    view_off_nadir: NotRequired["float"]
    """<p>The angle from the sensor between nadir (straight down) and the scene center. Measured in degrees (0-90).</p>"""
    view_sun_azimuth: NotRequired["float"]
    """<p>The sun azimuth angle. From the scene center point on the ground, this is the angle between truth north and the sun. Measured clockwise in degrees (0-360).</p>"""
    view_sun_elevation: NotRequired["float"]
    """<p>The sun elevation angle. The angle from the tangent of the scene center point to the sun. Measured from the horizon in degrees (-90-90). Negative values indicate the sun is below the horizon, e.g. sun elevation of -10° means the data was captured during <a href=\"https://www.timeanddate.com/astronomy/different-types-twilight.html\">nautical twilight</a>.</p>"""
    platform: NotRequired["str"]
    """<p>Platform property. Platform refers to the unique name of the specific platform the instrument is attached to. For satellites it is the name of the satellite, eg. landsat-8 (Landsat-8), sentinel-2a.</p>"""
    landsat_cloud_cover_land: NotRequired["float"]
    """<p>Land cloud cover for Landsat Data Collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Properties) -> dict:
    out: dict = {}
    if "eo_cloud_cover" in value:
        out["EoCloudCover"] = value["eo_cloud_cover"]
    if "view_off_nadir" in value:
        out["ViewOffNadir"] = value["view_off_nadir"]
    if "view_sun_azimuth" in value:
        out["ViewSunAzimuth"] = value["view_sun_azimuth"]
    if "view_sun_elevation" in value:
        out["ViewSunElevation"] = value["view_sun_elevation"]
    if "platform" in value:
        out["Platform"] = value["platform"]
    if "landsat_cloud_cover_land" in value:
        out["LandsatCloudCoverLand"] = value["landsat_cloud_cover_land"]
    return out


def deserialize_json(data: dict) -> Properties:
    out: Properties = {}  # type: ignore[typeddict-item]
    if "EoCloudCover" in data:
        out["eo_cloud_cover"] = data["EoCloudCover"]
    if "ViewOffNadir" in data:
        out["view_off_nadir"] = data["ViewOffNadir"]
    if "ViewSunAzimuth" in data:
        out["view_sun_azimuth"] = data["ViewSunAzimuth"]
    if "ViewSunElevation" in data:
        out["view_sun_elevation"] = data["ViewSunElevation"]
    if "Platform" in data:
        out["platform"] = data["Platform"]
    if "LandsatCloudCoverLand" in data:
        out["landsat_cloud_cover_land"] = data["LandsatCloudCoverLand"]
    return out
