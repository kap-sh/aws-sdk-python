"""Generated from Smithy shape ``com.amazonaws.fms#GetComplianceDetailResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.policy_compliance_detail


class GetComplianceDetailResponse(TypedDict):
    policy_compliance_detail: NotRequired[
        "aws_sdk_fms.types.policy_compliance_detail.PolicyComplianceDetail"
    ]
    """<p>Information about the resources and the policy that you specified in the <code>GetComplianceDetail</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetComplianceDetailResponse) -> dict:
    out: dict = {}
    if "policy_compliance_detail" in value:
        import aws_sdk_fms.types.policy_compliance_detail

        out["PolicyComplianceDetail"] = (
            aws_sdk_fms.types.policy_compliance_detail.serialize_aws_json_1_1(
                value["policy_compliance_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetComplianceDetailResponse:
    out: GetComplianceDetailResponse = {}  # type: ignore[typeddict-item]
    if "PolicyComplianceDetail" in data:
        import aws_sdk_fms.types.policy_compliance_detail

        out["policy_compliance_detail"] = (
            aws_sdk_fms.types.policy_compliance_detail.deserialize_aws_json_1_1(
                data["PolicyComplianceDetail"]
            )
        )
    return out
