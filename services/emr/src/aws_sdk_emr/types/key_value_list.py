"""Generated from Smithy shape ``com.amazonaws.emr#KeyValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.key_value

KeyValueList: TypeAlias = list["aws_sdk_emr.types.key_value.KeyValue"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyValueList) -> list:
    import aws_sdk_emr.types.key_value

    out: list = []
    for item in value:
        out.append(aws_sdk_emr.types.key_value.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> KeyValueList:
    import aws_sdk_emr.types.key_value

    out: KeyValueList = []
    for item in data:
        out.append(aws_sdk_emr.types.key_value.deserialize_aws_json_1_1(item))
    return out
