"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#DescribeHomeRegionControlsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhub_config.types.home_region_controls
    import capo_migrationhub_config.types.token


class DescribeHomeRegionControlsResult(TypedDict, closed=True):
    home_region_controls: NotRequired[
        "capo_migrationhub_config.types.home_region_controls.HomeRegionControls"
    ]
    """<p>An array that contains your <code>HomeRegionControl</code> objects.</p>"""
    next_token: NotRequired["capo_migrationhub_config.types.token.Token"]
    """<p>If a <code>NextToken</code> was returned by a previous call, more results are available. To retrieve the next page of results, make the call again using the returned token in <code>NextToken</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHomeRegionControlsResult) -> dict:
    out: dict = {}
    if "home_region_controls" in value:
        import capo_migrationhub_config.types.home_region_controls

        out["HomeRegionControls"] = (
            capo_migrationhub_config.types.home_region_controls.serialize_aws_json_1_1(
                value["home_region_controls"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHomeRegionControlsResult:
    out: DescribeHomeRegionControlsResult = {}  # type: ignore[typeddict-item]
    if "HomeRegionControls" in data:
        import capo_migrationhub_config.types.home_region_controls

        out["home_region_controls"] = (
            capo_migrationhub_config.types.home_region_controls.deserialize_aws_json_1_1(
                data["HomeRegionControls"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
