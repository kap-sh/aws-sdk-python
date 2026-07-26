"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#CoverageTimes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_contacts.types.coverage_time

CoverageTimes: TypeAlias = list["capo_ssm_contacts.types.coverage_time.CoverageTime"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CoverageTimes) -> list:
    import capo_ssm_contacts.types.coverage_time

    out: list = []
    for item in value:
        out.append(capo_ssm_contacts.types.coverage_time.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CoverageTimes:
    import capo_ssm_contacts.types.coverage_time

    out: CoverageTimes = []
    for item in data:
        out.append(capo_ssm_contacts.types.coverage_time.deserialize_aws_json_1_1(item))
    return out
