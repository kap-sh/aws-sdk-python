"""Generated from Smithy shape ``com.amazonaws.health#DescribeHealthServiceStatusForOrganizationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_health.types.health_service_access_status_for_organization


class DescribeHealthServiceStatusForOrganizationResponse(TypedDict):
    health_service_access_status_for_organization: NotRequired[
        "aws_sdk_health.types.health_service_access_status_for_organization.healthServiceAccessStatusForOrganization"
    ]
    """<p>Information about the status of enabling or disabling the Health organizational view feature in your organization.</p> <p>Valid values are <code>ENABLED | DISABLED | PENDING</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeHealthServiceStatusForOrganizationResponse,
) -> dict:
    out: dict = {}
    if "health_service_access_status_for_organization" in value:
        out["healthServiceAccessStatusForOrganization"] = value[
            "health_service_access_status_for_organization"
        ]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeHealthServiceStatusForOrganizationResponse:
    out: DescribeHealthServiceStatusForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if "healthServiceAccessStatusForOrganization" in data:
        out["health_service_access_status_for_organization"] = data[
            "healthServiceAccessStatusForOrganization"
        ]
    return out
