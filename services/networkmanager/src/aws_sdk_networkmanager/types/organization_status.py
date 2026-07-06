"""Generated from Smithy shape ``com.amazonaws.networkmanager#OrganizationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.account_status_list
    import aws_sdk_networkmanager.types.organization_aws_service_access_status
    import aws_sdk_networkmanager.types.organization_id
    import aws_sdk_networkmanager.types.slr_deployment_status


class OrganizationStatus(TypedDict, closed=True):
    organization_id: NotRequired[
        "aws_sdk_networkmanager.types.organization_id.OrganizationId"
    ]
    """<p>The ID of an Amazon Web Services Organization.</p>"""
    organization_aws_service_access_status: NotRequired[
        "aws_sdk_networkmanager.types.organization_aws_service_access_status.OrganizationAwsServiceAccessStatus"
    ]
    """<p>The status of the organization's AWS service access. This will be <code>ENABLED</code> or <code>DISABLED</code>.</p>"""
    slr_deployment_status: NotRequired[
        "aws_sdk_networkmanager.types.slr_deployment_status.SLRDeploymentStatus"
    ]
    """<p>The status of the SLR deployment for the account. This will be either <code>SUCCEEDED</code> or <code>IN_PROGRESS</code>.</p>"""
    account_status_list: NotRequired[
        "aws_sdk_networkmanager.types.account_status_list.AccountStatusList"
    ]
    """<p>The current service-linked role (SLR) deployment status for an Amazon Web Services Organization's accounts. This will be either <code>SUCCEEDED</code> or <code>IN_PROGRESS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationStatus) -> dict:
    out: dict = {}
    if "organization_id" in value:
        out["OrganizationId"] = value["organization_id"]
    if "organization_aws_service_access_status" in value:
        out["OrganizationAwsServiceAccessStatus"] = value[
            "organization_aws_service_access_status"
        ]
    if "slr_deployment_status" in value:
        out["SLRDeploymentStatus"] = value["slr_deployment_status"]
    if "account_status_list" in value:
        import aws_sdk_networkmanager.types.account_status_list

        out["AccountStatusList"] = (
            aws_sdk_networkmanager.types.account_status_list.serialize_json(
                value["account_status_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> OrganizationStatus:
    out: OrganizationStatus = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    if "OrganizationAwsServiceAccessStatus" in data:
        out["organization_aws_service_access_status"] = data[
            "OrganizationAwsServiceAccessStatus"
        ]
    if "SLRDeploymentStatus" in data:
        out["slr_deployment_status"] = data["SLRDeploymentStatus"]
    if "AccountStatusList" in data:
        import aws_sdk_networkmanager.types.account_status_list

        out["account_status_list"] = (
            aws_sdk_networkmanager.types.account_status_list.deserialize_json(
                data["AccountStatusList"]
            )
        )
    return out
