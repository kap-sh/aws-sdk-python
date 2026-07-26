"""Generated from Smithy shape ``com.amazonaws.ecr#FindingSeverityCounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.finding_severity
    import capo_ecr.types.severity_count

FindingSeverityCounts: TypeAlias = dict[
    "capo_ecr.types.finding_severity.FindingSeverity",
    "capo_ecr.types.severity_count.SeverityCount",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: FindingSeverityCounts) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_ecr.types.finding_severity

        out[capo_ecr.types.finding_severity.serialize_aws_json_1_1(key)] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> FindingSeverityCounts:
    out: FindingSeverityCounts = {}
    for key, value in data.items():
        import capo_ecr.types.finding_severity

        out[capo_ecr.types.finding_severity.deserialize_aws_json_1_1(key)] = value
    return out
