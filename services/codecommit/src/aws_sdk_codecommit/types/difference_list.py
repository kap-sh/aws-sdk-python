"""Generated from Smithy shape ``com.amazonaws.codecommit#DifferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.difference

DifferenceList: TypeAlias = list["aws_sdk_codecommit.types.difference.Difference"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DifferenceList) -> list:
    import aws_sdk_codecommit.types.difference

    out: list = []
    for item in value:
        out.append(aws_sdk_codecommit.types.difference.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DifferenceList:
    import aws_sdk_codecommit.types.difference

    out: DifferenceList = []
    for item in data:
        out.append(aws_sdk_codecommit.types.difference.deserialize_aws_json_1_1(item))
    return out
