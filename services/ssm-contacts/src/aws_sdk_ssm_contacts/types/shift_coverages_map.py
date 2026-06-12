"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ShiftCoveragesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.coverage_times
    import aws_sdk_ssm_contacts.types.day_of_week

ShiftCoveragesMap: TypeAlias = dict[
    "aws_sdk_ssm_contacts.types.day_of_week.DayOfWeek",
    "aws_sdk_ssm_contacts.types.coverage_times.CoverageTimes",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ShiftCoveragesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_ssm_contacts.types.coverage_times
        import aws_sdk_ssm_contacts.types.day_of_week

        out[aws_sdk_ssm_contacts.types.day_of_week.serialize_aws_json_1_1(key)] = (
            aws_sdk_ssm_contacts.types.coverage_times.serialize_aws_json_1_1(value)
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ShiftCoveragesMap:
    out: ShiftCoveragesMap = {}
    for key, value in data.items():
        import aws_sdk_ssm_contacts.types.coverage_times
        import aws_sdk_ssm_contacts.types.day_of_week

        out[aws_sdk_ssm_contacts.types.day_of_week.deserialize_aws_json_1_1(key)] = (
            aws_sdk_ssm_contacts.types.coverage_times.deserialize_aws_json_1_1(value)
        )
    return out
