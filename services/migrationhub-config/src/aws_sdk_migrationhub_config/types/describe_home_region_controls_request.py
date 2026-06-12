"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#DescribeHomeRegionControlsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhub_config.types.control_id
    import aws_sdk_migrationhub_config.types.describe_home_region_controls_max_results
    import aws_sdk_migrationhub_config.types.home_region
    import aws_sdk_migrationhub_config.types.target
    import aws_sdk_migrationhub_config.types.token


class DescribeHomeRegionControlsRequest(TypedDict):
    control_id: NotRequired["aws_sdk_migrationhub_config.types.control_id.ControlId"]
    """<p>The <code>ControlID</code> is a unique identifier string of your <code>HomeRegionControl</code> object.</p>"""
    home_region: NotRequired["aws_sdk_migrationhub_config.types.home_region.HomeRegion"]
    """<p>The name of the home region you'd like to view.</p>"""
    target: NotRequired["aws_sdk_migrationhub_config.types.target.Target"]
    """<p>The target parameter specifies the identifier to which the home region is applied, which is always of type <code>ACCOUNT</code>. It applies the home region to the current <code>ACCOUNT</code>.</p>"""
    max_results: NotRequired[
        "aws_sdk_migrationhub_config.types.describe_home_region_controls_max_results.DescribeHomeRegionControlsMaxResults"
    ]
    """<p>The maximum number of filtering results to display per page. </p>"""
    next_token: NotRequired["aws_sdk_migrationhub_config.types.token.Token"]
    """<p>If a <code>NextToken</code> was returned by a previous call, more results are available. To retrieve the next page of results, make the call again using the returned token in <code>NextToken</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHomeRegionControlsRequest) -> dict:
    out: dict = {}
    if "control_id" in value:
        out["ControlId"] = value["control_id"]
    if "home_region" in value:
        out["HomeRegion"] = value["home_region"]
    if "target" in value:
        import aws_sdk_migrationhub_config.types.target

        out["Target"] = aws_sdk_migrationhub_config.types.target.serialize_aws_json_1_1(
            value["target"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHomeRegionControlsRequest:
    out: DescribeHomeRegionControlsRequest = {}  # type: ignore[typeddict-item]
    if "ControlId" in data:
        out["control_id"] = data["ControlId"]
    if "HomeRegion" in data:
        out["home_region"] = data["HomeRegion"]
    if "Target" in data:
        import aws_sdk_migrationhub_config.types.target

        out["target"] = (
            aws_sdk_migrationhub_config.types.target.deserialize_aws_json_1_1(
                data["Target"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
