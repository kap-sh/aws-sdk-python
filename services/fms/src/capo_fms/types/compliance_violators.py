"""Generated from Smithy shape ``com.amazonaws.fms#ComplianceViolators``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.compliance_violator

ComplianceViolators: TypeAlias = list[
    "capo_fms.types.compliance_violator.ComplianceViolator"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceViolators) -> list:
    import capo_fms.types.compliance_violator

    out: list = []
    for item in value:
        out.append(capo_fms.types.compliance_violator.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ComplianceViolators:
    import capo_fms.types.compliance_violator

    out: ComplianceViolators = []
    for item in data:
        out.append(capo_fms.types.compliance_violator.deserialize_aws_json_1_1(item))
    return out
