"""Generated from Smithy shape ``com.amazonaws.appstream#ArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.arn

ArnList: TypeAlias = list["capo_appstream.types.arn.Arn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ArnList:
    return list(data)
