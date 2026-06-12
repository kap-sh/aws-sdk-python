"""Generated from Smithy shape ``com.amazonaws.translate#TermList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_translate.types.term

TermList: TypeAlias = list["aws_sdk_translate.types.term.Term"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TermList) -> list:
    import aws_sdk_translate.types.term

    out: list = []
    for item in value:
        out.append(aws_sdk_translate.types.term.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TermList:
    import aws_sdk_translate.types.term

    out: TermList = []
    for item in data:
        out.append(aws_sdk_translate.types.term.deserialize_aws_json_1_1(item))
    return out
