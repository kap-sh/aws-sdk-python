"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ResourceProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class ResourceProperty(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of this property of the resource.</p>"""
    last_reported_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the information about this resource property was last updated.</p>"""
    data: NotRequired["object"]
    """<p>Details about this property. The content of this field is a JSON object that varies based on the resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceProperty) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "last_reported_at" in value:
        import aws_sdk_resource_explorer_2.types._prelude.timestamp

        out["LastReportedAt"] = (
            aws_sdk_resource_explorer_2.types._prelude.timestamp.serialize_json(
                value["last_reported_at"]
            )
        )
    if "data" in value:
        out["Data"] = value["data"]
    return out


def deserialize_json(data: dict) -> ResourceProperty:
    out: ResourceProperty = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "LastReportedAt" in data:
        import aws_sdk_resource_explorer_2.types._prelude.timestamp

        out["last_reported_at"] = (
            aws_sdk_resource_explorer_2.types._prelude.timestamp.deserialize_json(
                data["LastReportedAt"]
            )
        )
    if "Data" in data:
        out["data"] = data["Data"]
    return out
