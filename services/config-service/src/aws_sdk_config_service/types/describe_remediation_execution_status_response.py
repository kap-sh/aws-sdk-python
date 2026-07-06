"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeRemediationExecutionStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.remediation_execution_statuses
    import aws_sdk_config_service.types.string


class DescribeRemediationExecutionStatusResponse(TypedDict, closed=True):
    remediation_execution_statuses: NotRequired[
        "aws_sdk_config_service.types.remediation_execution_statuses.RemediationExecutionStatuses"
    ]
    """<p>Returns a list of remediation execution statuses objects.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRemediationExecutionStatusResponse) -> dict:
    out: dict = {}
    if "remediation_execution_statuses" in value:
        import aws_sdk_config_service.types.remediation_execution_statuses

        out["RemediationExecutionStatuses"] = (
            aws_sdk_config_service.types.remediation_execution_statuses.serialize_aws_json_1_1(
                value["remediation_execution_statuses"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRemediationExecutionStatusResponse:
    out: DescribeRemediationExecutionStatusResponse = {}  # type: ignore[typeddict-item]
    if "RemediationExecutionStatuses" in data:
        import aws_sdk_config_service.types.remediation_execution_statuses

        out["remediation_execution_statuses"] = (
            aws_sdk_config_service.types.remediation_execution_statuses.deserialize_aws_json_1_1(
                data["RemediationExecutionStatuses"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
