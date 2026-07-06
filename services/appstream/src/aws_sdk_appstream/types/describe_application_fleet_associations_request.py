"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeApplicationFleetAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.arn
    import aws_sdk_appstream.types.integer
    import aws_sdk_appstream.types.name
    import aws_sdk_appstream.types.string


class DescribeApplicationFleetAssociationsRequest(TypedDict, closed=True):
    fleet_name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the fleet.</p>"""
    application_arn: NotRequired["aws_sdk_appstream.types.arn.Arn"]
    """<p>The ARN of the application.</p>"""
    max_results: NotRequired["aws_sdk_appstream.types.integer.Integer"]
    """<p>The maximum size of each page of results.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationFleetAssociationsRequest) -> dict:
    out: dict = {}
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationFleetAssociationsRequest:
    out: DescribeApplicationFleetAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "FleetName" in data:
        out["fleet_name"] = data["FleetName"]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
