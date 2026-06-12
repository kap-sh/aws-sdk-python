"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.status

DocumentStatusList: TypeAlias = list["aws_sdk_kendra.types.status.Status"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentStatusList) -> list:
    import aws_sdk_kendra.types.status

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.status.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentStatusList:
    import aws_sdk_kendra.types.status

    out: DocumentStatusList = []
    for item in data:
        out.append(aws_sdk_kendra.types.status.deserialize_aws_json_1_1(item))
    return out
