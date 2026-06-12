"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RecommendationDisruptionCompliance``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.compliance_status
    import aws_sdk_resiliencehub.types.seconds
    import aws_sdk_resiliencehub.types.string500


class RecommendationDisruptionCompliance(TypedDict):
    expected_compliance_status: (
        "aws_sdk_resiliencehub.types.compliance_status.ComplianceStatus"
    )
    """<p>The expected compliance status after applying the recommended configuration change.</p>"""
    expected_rto_in_secs: "aws_sdk_resiliencehub.types.seconds.Seconds"
    """<p>The expected RTO after applying the recommended configuration change.</p>"""
    expected_rto_description: NotRequired[
        "aws_sdk_resiliencehub.types.string500.String500"
    ]
    """<p>The expected Recovery Time Objective (RTO) description after applying the recommended configuration change.</p>"""
    expected_rpo_in_secs: "aws_sdk_resiliencehub.types.seconds.Seconds"
    """<p>The expected RPO after applying the recommended configuration change.</p>"""
    expected_rpo_description: NotRequired[
        "aws_sdk_resiliencehub.types.string500.String500"
    ]
    """<p>The expected Recovery Point Objective (RPO) description after applying the recommended configuration change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationDisruptionCompliance) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehub.types.compliance_status

    out["expectedComplianceStatus"] = (
        aws_sdk_resiliencehub.types.compliance_status.serialize_json(
            value["expected_compliance_status"]
        )
    )
    out["expectedRtoInSecs"] = value.get("expected_rto_in_secs", 0)
    if "expected_rto_description" in value:
        out["expectedRtoDescription"] = value["expected_rto_description"]
    out["expectedRpoInSecs"] = value.get("expected_rpo_in_secs", 0)
    if "expected_rpo_description" in value:
        out["expectedRpoDescription"] = value["expected_rpo_description"]
    return out


def deserialize_json(data: dict) -> RecommendationDisruptionCompliance:
    out: RecommendationDisruptionCompliance = {}  # type: ignore[typeddict-item]
    if "expectedComplianceStatus" in data:
        import aws_sdk_resiliencehub.types.compliance_status

        out["expected_compliance_status"] = (
            aws_sdk_resiliencehub.types.compliance_status.deserialize_json(
                data["expectedComplianceStatus"]
            )
        )
    else:
        raise DeserializationError(
            "RecommendationDisruptionCompliance.expected_compliance_status required"
        )
    if "expectedRtoInSecs" in data:
        out["expected_rto_in_secs"] = data["expectedRtoInSecs"]
    else:
        out["expected_rto_in_secs"] = 0
    if "expectedRtoDescription" in data:
        out["expected_rto_description"] = data["expectedRtoDescription"]
    if "expectedRpoInSecs" in data:
        out["expected_rpo_in_secs"] = data["expectedRpoInSecs"]
    else:
        out["expected_rpo_in_secs"] = 0
    if "expectedRpoDescription" in data:
        out["expected_rpo_description"] = data["expectedRpoDescription"]
    return out
