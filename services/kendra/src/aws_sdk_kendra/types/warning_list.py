"""Generated from Smithy shape ``com.amazonaws.kendra#WarningList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.warning

WarningList: TypeAlias = list["aws_sdk_kendra.types.warning.Warning"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WarningList) -> list:
    import aws_sdk_kendra.types.warning

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.warning.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> WarningList:
    import aws_sdk_kendra.types.warning

    out: WarningList = []
    for item in data:
        out.append(aws_sdk_kendra.types.warning.deserialize_aws_json_1_1(item))
    return out
