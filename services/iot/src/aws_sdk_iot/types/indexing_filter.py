"""Generated from Smithy shape ``com.amazonaws.iot#IndexingFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.connectivity_filter
    import aws_sdk_iot.types.geo_locations_filter
    import aws_sdk_iot.types.named_shadow_names_filter


class IndexingFilter(TypedDict):
    named_shadow_names: NotRequired[
        "aws_sdk_iot.types.named_shadow_names_filter.NamedShadowNamesFilter"
    ]
    r"""<p>The shadow names that you select to index. The default maximum number of shadow names for indexing is 10. To increase the limit, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/iot_device_management.html#fleet-indexing-limits\">Amazon Web Services IoT Device Management Quotas</a> in the <i>Amazon Web Services General Reference</i>. </p>"""
    geo_locations: NotRequired[
        "aws_sdk_iot.types.geo_locations_filter.GeoLocationsFilter"
    ]
    r"""<p>The list of geolocation targets that you select to index. The default maximum number of geolocation targets for indexing is <code>1</code>. To increase the limit, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/iot_device_management.html#fleet-indexing-limits\">Amazon Web Services IoT Device Management Quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    connectivity: NotRequired[
        "aws_sdk_iot.types.connectivity_filter.ConnectivityFilter"
    ]
    """<p>Provides additional connectivity filter selections for the fleet indexing configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IndexingFilter) -> dict:
    out: dict = {}
    if "named_shadow_names" in value:
        import aws_sdk_iot.types.named_shadow_names_filter

        out["namedShadowNames"] = (
            aws_sdk_iot.types.named_shadow_names_filter.serialize_json(
                value["named_shadow_names"]
            )
        )
    if "geo_locations" in value:
        import aws_sdk_iot.types.geo_locations_filter

        out["geoLocations"] = aws_sdk_iot.types.geo_locations_filter.serialize_json(
            value["geo_locations"]
        )
    if "connectivity" in value:
        import aws_sdk_iot.types.connectivity_filter

        out["connectivity"] = aws_sdk_iot.types.connectivity_filter.serialize_json(
            value["connectivity"]
        )
    return out


def deserialize_json(data: dict) -> IndexingFilter:
    out: IndexingFilter = {}  # type: ignore[typeddict-item]
    if "namedShadowNames" in data:
        import aws_sdk_iot.types.named_shadow_names_filter

        out["named_shadow_names"] = (
            aws_sdk_iot.types.named_shadow_names_filter.deserialize_json(
                data["namedShadowNames"]
            )
        )
    if "geoLocations" in data:
        import aws_sdk_iot.types.geo_locations_filter

        out["geo_locations"] = aws_sdk_iot.types.geo_locations_filter.deserialize_json(
            data["geoLocations"]
        )
    if "connectivity" in data:
        import aws_sdk_iot.types.connectivity_filter

        out["connectivity"] = aws_sdk_iot.types.connectivity_filter.deserialize_json(
            data["connectivity"]
        )
    return out
