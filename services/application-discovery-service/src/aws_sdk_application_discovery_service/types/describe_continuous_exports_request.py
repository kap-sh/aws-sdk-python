"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeContinuousExportsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.continuous_export_ids
    import aws_sdk_application_discovery_service.types.describe_continuous_exports_max_results
    import aws_sdk_application_discovery_service.types.next_token


class DescribeContinuousExportsRequest(TypedDict, closed=True):
    export_ids: NotRequired[
        "aws_sdk_application_discovery_service.types.continuous_export_ids.ContinuousExportIds"
    ]
    """<p>The unique IDs assigned to the exports.</p>"""
    max_results: NotRequired[
        "aws_sdk_application_discovery_service.types.describe_continuous_exports_max_results.DescribeContinuousExportsMaxResults"
    ]
    """<p>A number between 1 and 100 specifying the maximum number of continuous export descriptions returned.</p>"""
    next_token: NotRequired[
        "aws_sdk_application_discovery_service.types.next_token.NextToken"
    ]
    """<p>The token from the previous call to <code>DescribeExportTasks</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeContinuousExportsRequest) -> dict:
    out: dict = {}
    if "export_ids" in value:
        import aws_sdk_application_discovery_service.types.continuous_export_ids

        out["exportIds"] = (
            aws_sdk_application_discovery_service.types.continuous_export_ids.serialize_aws_json_1_1(
                value["export_ids"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeContinuousExportsRequest:
    out: DescribeContinuousExportsRequest = {}  # type: ignore[typeddict-item]
    if "exportIds" in data:
        import aws_sdk_application_discovery_service.types.continuous_export_ids

        out["export_ids"] = (
            aws_sdk_application_discovery_service.types.continuous_export_ids.deserialize_aws_json_1_1(
                data["exportIds"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
