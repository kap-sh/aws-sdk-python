"""Generated from Smithy shape ``com.amazonaws.emr#KeyValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.key_value

KeyValueList: TypeAlias = list["capo_emr.types.key_value.KeyValue"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyValueList) -> list:
    import capo_emr.types.key_value

    out: list = []
    for item in value:
        out.append(capo_emr.types.key_value.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> KeyValueList:
    import capo_emr.types.key_value

    out: KeyValueList = []
    for item in data:
        out.append(capo_emr.types.key_value.deserialize_aws_json_1_1(item))
    return out
