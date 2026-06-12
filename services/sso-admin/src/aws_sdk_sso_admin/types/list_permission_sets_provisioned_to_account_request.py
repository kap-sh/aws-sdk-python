"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListPermissionSetsProvisionedToAccountRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.account_id
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.max_results
    import aws_sdk_sso_admin.types.provisioning_status
    import aws_sdk_sso_admin.types.token


class ListPermissionSetsProvisionedToAccountRequest(TypedDict):
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    account_id: "aws_sdk_sso_admin.types.account_id.AccountId"
    """<p>The identifier of the Amazon Web Services account from which to list the assignments.</p>"""
    provisioning_status: NotRequired[
        "aws_sdk_sso_admin.types.provisioning_status.ProvisioningStatus"
    ]
    """<p>The status object for the permission set provisioning operation.</p>"""
    max_results: NotRequired["aws_sdk_sso_admin.types.max_results.MaxResults"]
    """<p>The maximum number of results to display for the assignment.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListPermissionSetsProvisionedToAccountRequest,
) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["AccountId"] = value["account_id"]
    if "provisioning_status" in value:
        import aws_sdk_sso_admin.types.provisioning_status

        out["ProvisioningStatus"] = (
            aws_sdk_sso_admin.types.provisioning_status.serialize_aws_json_1_1(
                value["provisioning_status"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListPermissionSetsProvisionedToAccountRequest:
    out: ListPermissionSetsProvisionedToAccountRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "ListPermissionSetsProvisionedToAccountRequest.instance_arn required"
        )
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError(
            "ListPermissionSetsProvisionedToAccountRequest.account_id required"
        )
    if "ProvisioningStatus" in data:
        import aws_sdk_sso_admin.types.provisioning_status

        out["provisioning_status"] = (
            aws_sdk_sso_admin.types.provisioning_status.deserialize_aws_json_1_1(
                data["ProvisioningStatus"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
