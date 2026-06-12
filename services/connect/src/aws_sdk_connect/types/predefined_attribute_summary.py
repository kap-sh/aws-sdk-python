"""Generated from Smithy shape ``com.amazonaws.connect#PredefinedAttributeSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.predefined_attribute_name
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.timestamp


class PredefinedAttributeSummary(TypedDict):
    name: NotRequired[
        "aws_sdk_connect.types.predefined_attribute_name.PredefinedAttributeName"
    ]
    """<p>The name of the predefined attribute.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>Last modified time.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>Last modified region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredefinedAttributeSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
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
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
