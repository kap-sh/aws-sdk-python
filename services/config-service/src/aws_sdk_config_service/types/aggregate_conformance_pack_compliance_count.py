"""Generated from Smithy shape ``com.amazonaws.configservice#AggregateConformancePackComplianceCount``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.integer


class AggregateConformancePackComplianceCount(TypedDict):
    compliant_conformance_pack_count: "aws_sdk_config_service.types.integer.Integer"
    """<p>Number of compliant conformance packs.</p>"""
    non_compliant_conformance_pack_count: "aws_sdk_config_service.types.integer.Integer"
    """<p>Number of noncompliant conformance packs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateConformancePackComplianceCount) -> dict:
    out: dict = {}
    out["CompliantConformancePackCount"] = value.get(
        "compliant_conformance_pack_count", 0
    )
    out["NonCompliantConformancePackCount"] = value.get(
        "non_compliant_conformance_pack_count", 0
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregateConformancePackComplianceCount:
    out: AggregateConformancePackComplianceCount = {}  # type: ignore[typeddict-item]
    if "CompliantConformancePackCount" in data:
        out["compliant_conformance_pack_count"] = data["CompliantConformancePackCount"]
    else:
        out["compliant_conformance_pack_count"] = 0
    if "NonCompliantConformancePackCount" in data:
        out["non_compliant_conformance_pack_count"] = data[
            "NonCompliantConformancePackCount"
        ]
    else:
        out["non_compliant_conformance_pack_count"] = 0
    return out
