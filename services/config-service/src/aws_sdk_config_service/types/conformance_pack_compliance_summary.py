"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackComplianceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_compliance_type
    import aws_sdk_config_service.types.conformance_pack_name


class ConformancePackComplianceSummary(TypedDict):
    conformance_pack_name: (
        "aws_sdk_config_service.types.conformance_pack_name.ConformancePackName"
    )
    """<p>The name of the conformance pack name.</p>"""
    conformance_pack_compliance_status: "aws_sdk_config_service.types.conformance_pack_compliance_type.ConformancePackComplianceType"
    """<p>The status of the conformance pack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackComplianceSummary) -> dict:
    out: dict = {}
    out["ConformancePackName"] = value["conformance_pack_name"]
    import aws_sdk_config_service.types.conformance_pack_compliance_type

    out["ConformancePackComplianceStatus"] = (
        aws_sdk_config_service.types.conformance_pack_compliance_type.serialize_aws_json_1_1(
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
        import aws_sdk_config_service.types.conformance_pack_compliance_type

        out["conformance_pack_compliance_status"] = (
            aws_sdk_config_service.types.conformance_pack_compliance_type.deserialize_aws_json_1_1(
                data["ConformancePackComplianceStatus"]
            )
        )
    else:
        raise DeserializationError(
            "ConformancePackComplianceSummary.conformance_pack_compliance_status required"
        )
    return out
