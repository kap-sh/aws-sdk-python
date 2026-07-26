"""Generated from Smithy shape ``com.amazonaws.connect#PredefinedAttributeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.predefined_attribute_name
    import capo_connect.types.region_name
    import capo_connect.types.timestamp


class PredefinedAttributeSummary(TypedDict, closed=True):
    name: NotRequired[
        "capo_connect.types.predefined_attribute_name.PredefinedAttributeName"
    ]
    """<p>The name of the predefined attribute.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>Last modified time.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>Last modified region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredefinedAttributeSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> PredefinedAttributeSummary:
    out: PredefinedAttributeSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "LastModifiedTime" in data:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
