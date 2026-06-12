"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListAccountAssignmentDeletionStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.max_results
    import aws_sdk_sso_admin.types.operation_status_filter
    import aws_sdk_sso_admin.types.token


class ListAccountAssignmentDeletionStatusRequest(TypedDict):
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    max_results: NotRequired["aws_sdk_sso_admin.types.max_results.MaxResults"]
    """<p>The maximum number of results to display for the assignment.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""
    filter: NotRequired[
        "aws_sdk_sso_admin.types.operation_status_filter.OperationStatusFilter"
    ]
    """<p>Filters results based on the passed attribute value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccountAssignmentDeletionStatusRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filter" in value:
        import aws_sdk_sso_admin.types.operation_status_filter

        out["Filter"] = (
            aws_sdk_sso_admin.types.operation_status_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccountAssignmentDeletionStatusRequest:
    out: ListAccountAssignmentDeletionStatusRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "ListAccountAssignmentDeletionStatusRequest.instance_arn required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filter" in data:
        import aws_sdk_sso_admin.types.operation_status_filter

        out["filter"] = (
            aws_sdk_sso_admin.types.operation_status_filter.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    return out
