"""Generated from Smithy shape ``com.amazonaws.acm#GeneralNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.general_name

GeneralNameList: TypeAlias = list["capo_acm.types.general_name.GeneralName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeneralNameList) -> list:
    import capo_acm.types.general_name

    out: list = []
    for item in value:
        out.append(capo_acm.types.general_name.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GeneralNameList:
    import capo_acm.types.general_name

    out: GeneralNameList = []
    for item in data:
        out.append(capo_acm.types.general_name.deserialize_aws_json_1_1(item))
    return out
