"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeExportConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.export_ids
    import aws_sdk_application_discovery_service.types.integer
    import aws_sdk_application_discovery_service.types.next_token


class DescribeExportConfigurationsRequest(TypedDict, closed=True):
    export_ids: NotRequired[
        "aws_sdk_application_discovery_service.types.export_ids.ExportIds"
    ]
    """<p>A list of continuous export IDs to search for.</p>"""
    max_results: "aws_sdk_application_discovery_service.types.integer.Integer"
    """<p>A number between 1 and 100 specifying the maximum number of continuous export descriptions returned.</p>"""
    next_token: NotRequired[
        "aws_sdk_application_discovery_service.types.next_token.NextToken"
    ]
    """<p>The token from the previous call to describe-export-tasks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExportConfigurationsRequest) -> dict:
    out: dict = {}
    if "export_ids" in value:
        import aws_sdk_application_discovery_service.types.export_ids

        out["exportIds"] = (
            aws_sdk_application_discovery_service.types.export_ids.serialize_aws_json_1_1(
                value["export_ids"]
            )
        )
    out["maxResults"] = value.get("max_results", 0)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExportConfigurationsRequest:
    out: DescribeExportConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "exportIds" in data:
        import aws_sdk_application_discovery_service.types.export_ids

        out["export_ids"] = (
            aws_sdk_application_discovery_service.types.export_ids.deserialize_aws_json_1_1(
                data["exportIds"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 0
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
