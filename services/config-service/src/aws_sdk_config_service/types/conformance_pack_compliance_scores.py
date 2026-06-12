"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackComplianceScores``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_compliance_score

ConformancePackComplianceScores: TypeAlias = list[
    "aws_sdk_config_service.types.conformance_pack_compliance_score.ConformancePackComplianceScore"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackComplianceScores) -> list:
    import aws_sdk_config_service.types.conformance_pack_compliance_score

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.conformance_pack_compliance_score.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConformancePackComplianceScores:
    import aws_sdk_config_service.types.conformance_pack_compliance_score

    out: ConformancePackComplianceScores = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.conformance_pack_compliance_score.deserialize_aws_json_1_1(
                item
            )
        )
    return out
