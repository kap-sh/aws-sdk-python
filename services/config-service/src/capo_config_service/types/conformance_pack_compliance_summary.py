"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackComplianceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_compliance_type
    import capo_config_service.types.conformance_pack_name


class ConformancePackComplianceSummary(TypedDict, closed=True):
    conformance_pack_name: (
        "capo_config_service.types.conformance_pack_name.ConformancePackName"
    )
    """<p>The name of the conformance pack name.</p>"""
    conformance_pack_compliance_status: "capo_config_service.types.conformance_pack_compliance_type.ConformancePackComplianceType"
    """<p>The status of the conformance pack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackComplianceSummary) -> dict:
    out: dict = {}
    out["ConformancePackName"] = value["conformance_pack_name"]
    import capo_config_service.types.conformance_pack_compliance_type

    out["ConformancePackComplianceStatus"] = (
        capo_config_service.types.conformance_pack_compliance_type.serialize_aws_json_1_1(
            value["conformance_pack_compliance_status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackComplianceSummary:
    out: ConformancePackComplianceSummary = {}  # type: ignore[typeddict-item]
    if "ConformancePackName" in data:
        out["conformance_pack_name"] = data["ConformancePackName"]
    else:
        raise DeserializationError(
            "ConformancePackComplianceSummary.conformance_pack_name required"
        )
    if "ConformancePackComplianceStatus" in data:
        import capo_config_service.types.conformance_pack_compliance_type

        out["conformance_pack_compliance_status"] = (
            capo_config_service.types.conformance_pack_compliance_type.deserialize_aws_json_1_1(
                data["ConformancePackComplianceStatus"]
            )
        )
    else:
        raise DeserializationError(
            "ConformancePackComplianceSummary.conformance_pack_compliance_status required"
        )
    return out
