"""Generated from Smithy shape ``com.amazonaws.cloudhsm#AZList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.az

AZList: TypeAlias = list["aws_sdk_cloudhsm.types.az.AZ"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AZList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AZList:
    return list(data)
