"""Generated from Smithy shape ``com.amazonaws.kendra#HighlightList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.highlight

HighlightList: TypeAlias = list["capo_kendra.types.highlight.Highlight"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HighlightList) -> list:
    import capo_kendra.types.highlight

    out: list = []
    for item in value:
        out.append(capo_kendra.types.highlight.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> HighlightList:
    import capo_kendra.types.highlight

    out: HighlightList = []
    for item in data:
        out.append(capo_kendra.types.highlight.deserialize_aws_json_1_1(item))
    return out
