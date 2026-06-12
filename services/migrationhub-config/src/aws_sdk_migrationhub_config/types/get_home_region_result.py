"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#GetHomeRegionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhub_config.types.home_region


class GetHomeRegionResult(TypedDict):
    home_region: NotRequired["aws_sdk_migrationhub_config.types.home_region.HomeRegion"]
    """<p>The name of the home region of the calling account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetHomeRegionResult) -> dict:
    out: dict = {}
    if "home_region" in value:
        out["HomeRegion"] = value["home_region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetHomeRegionResult:
    out: GetHomeRegionResult = {}  # type: ignore[typeddict-item]
    if "HomeRegion" in data:
        out["home_region"] = data["HomeRegion"]
    return out
