"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AssociatedApplication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.string


class AssociatedApplication(TypedDict, closed=True):
    name: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """<p> Name of the application as defined in Application Discovery Service. </p>"""
    id: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """<p> ID of the application as defined in Application Discovery Service. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedApplication) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> AssociatedApplication:
    out: AssociatedApplication = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "id" in data:
        out["id"] = data["id"]
    return out
