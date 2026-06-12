"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunFindingCounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.finding_count
    import aws_sdk_inspector.types.severity

AssessmentRunFindingCounts: TypeAlias = dict[
    "aws_sdk_inspector.types.severity.Severity",
    "aws_sdk_inspector.types.finding_count.FindingCount",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: AssessmentRunFindingCounts) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_inspector.types.severity

        out[aws_sdk_inspector.types.severity.serialize_aws_json_1_1(key)] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentRunFindingCounts:
    out: AssessmentRunFindingCounts = {}
    for key, value in data.items():
        import aws_sdk_inspector.types.severity

        out[aws_sdk_inspector.types.severity.deserialize_aws_json_1_1(key)] = value
    return out
