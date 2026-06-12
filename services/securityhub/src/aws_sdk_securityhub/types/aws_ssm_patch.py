"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsSsmPatch``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ssm_compliance_summary


class AwsSsmPatch(TypedDict):
    compliance_summary: NotRequired[
        "aws_sdk_securityhub.types.aws_ssm_compliance_summary.AwsSsmComplianceSummary"
    ]
    """<p>The compliance status details for the patch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsSsmPatch) -> dict:
    out: dict = {}
    if "compliance_summary" in value:
        import aws_sdk_securityhub.types.aws_ssm_compliance_summary

        out["ComplianceSummary"] = (
            aws_sdk_securityhub.types.aws_ssm_compliance_summary.serialize_json(
                value["compliance_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsSsmPatch:
    out: AwsSsmPatch = {}  # type: ignore[typeddict-item]
    if "ComplianceSummary" in data:
        import aws_sdk_securityhub.types.aws_ssm_compliance_summary

        out["compliance_summary"] = (
            aws_sdk_securityhub.types.aws_ssm_compliance_summary.deserialize_json(
                data["ComplianceSummary"]
            )
        )
    return out
