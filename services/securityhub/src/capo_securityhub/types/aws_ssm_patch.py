"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsSsmPatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ssm_compliance_summary


class AwsSsmPatch(TypedDict, closed=True):
    compliance_summary: NotRequired[
        "capo_securityhub.types.aws_ssm_compliance_summary.AwsSsmComplianceSummary"
    ]
    """<p>The compliance status details for the patch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsSsmPatch) -> dict:
    out: dict = {}
    if "compliance_summary" in value:
        import capo_securityhub.types.aws_ssm_compliance_summary

        out["ComplianceSummary"] = (
            capo_securityhub.types.aws_ssm_compliance_summary.serialize_json(
                value["compliance_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsSsmPatch:
    out: AwsSsmPatch = {}  # type: ignore[typeddict-item]
    if "ComplianceSummary" in data:
        import capo_securityhub.types.aws_ssm_compliance_summary

        out["compliance_summary"] = (
            capo_securityhub.types.aws_ssm_compliance_summary.deserialize_json(
                data["ComplianceSummary"]
            )
        )
    return out
