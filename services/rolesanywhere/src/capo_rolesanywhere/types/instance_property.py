"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#InstanceProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_rolesanywhere.types.instance_property_map


class InstanceProperty(TypedDict, closed=True):
    seen_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 time stamp of when the certificate was last used in a temporary credential request.</p>"""
    properties: NotRequired[
        "capo_rolesanywhere.types.instance_property_map.InstancePropertyMap"
    ]
    """<p>A list of instanceProperty objects. </p>"""
    failed: NotRequired["bool"]
    """<p>Indicates whether the temporary credential request was successful. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceProperty) -> dict:
    out: dict = {}
    if "seen_at" in value:
        import capo_rolesanywhere.types._prelude.timestamp

        out["seenAt"] = capo_rolesanywhere.types._prelude.timestamp.serialize_json(
            value["seen_at"]
        )
    if "properties" in value:
        import capo_rolesanywhere.types.instance_property_map

        out["properties"] = (
            capo_rolesanywhere.types.instance_property_map.serialize_json(
                value["properties"]
            )
        )
    if "failed" in value:
        out["failed"] = value["failed"]
    return out


def deserialize_json(data: dict) -> InstanceProperty:
    out: InstanceProperty = {}  # type: ignore[typeddict-item]
    if "seenAt" in data:
        import capo_rolesanywhere.types._prelude.timestamp

        out["seen_at"] = capo_rolesanywhere.types._prelude.timestamp.deserialize_json(
            data["seenAt"]
        )
    if "properties" in data:
        import capo_rolesanywhere.types.instance_property_map

        out["properties"] = (
            capo_rolesanywhere.types.instance_property_map.deserialize_json(
                data["properties"]
            )
        )
    if "failed" in data:
        out["failed"] = data["failed"]
    return out
