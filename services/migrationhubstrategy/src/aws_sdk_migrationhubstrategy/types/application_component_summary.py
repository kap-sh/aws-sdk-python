"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ApplicationComponentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.app_type
    import aws_sdk_migrationhubstrategy.types.integer


class ApplicationComponentSummary(TypedDict, closed=True):
    app_type: NotRequired["aws_sdk_migrationhubstrategy.types.app_type.AppType"]
    """<p> Contains the name of application types. </p>"""
    count: NotRequired["aws_sdk_migrationhubstrategy.types.integer.Integer"]
    """<p> Contains the count of application type. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationComponentSummary) -> dict:
    out: dict = {}
    if "app_type" in value:
        out["appType"] = value["app_type"]
    if "count" in value:
        out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> ApplicationComponentSummary:
    out: ApplicationComponentSummary = {}  # type: ignore[typeddict-item]
    if "appType" in data:
        out["app_type"] = data["appType"]
    if "count" in data:
        out["count"] = data["count"]
    return out
