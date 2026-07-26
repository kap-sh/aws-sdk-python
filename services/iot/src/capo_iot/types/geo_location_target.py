"""Generated from Smithy shape ``com.amazonaws.iot#GeoLocationTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.target_field_name
    import capo_iot.types.target_field_order


class GeoLocationTarget(TypedDict, closed=True):
    name: NotRequired["capo_iot.types.target_field_name.TargetFieldName"]
    """<p>The <code>name</code> of the geolocation target field. If the target field is part of a named shadow, you must select the named shadow using the <code>namedShadow</code> filter.</p>"""
    order: NotRequired["capo_iot.types.target_field_order.TargetFieldOrder"]
    """<p>The <code>order</code> of the geolocation target field. This field is optional. The default value is <code>LatLon</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeoLocationTarget) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "order" in value:
        import capo_iot.types.target_field_order

        out["order"] = capo_iot.types.target_field_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> GeoLocationTarget:
    out: GeoLocationTarget = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "order" in data:
        import capo_iot.types.target_field_order

        out["order"] = capo_iot.types.target_field_order.deserialize_json(data["order"])
    return out
