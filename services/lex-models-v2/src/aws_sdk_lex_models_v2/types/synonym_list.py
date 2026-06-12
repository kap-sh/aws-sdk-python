"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SynonymList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.sample_value

SynonymList: TypeAlias = list["aws_sdk_lex_models_v2.types.sample_value.SampleValue"]


# --- restJson1 ser/de ---
def serialize_json(value: SynonymList) -> list:
    import aws_sdk_lex_models_v2.types.sample_value

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_models_v2.types.sample_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> SynonymList:
    import aws_sdk_lex_models_v2.types.sample_value

    out: SynonymList = []
    for item in data:
        out.append(aws_sdk_lex_models_v2.types.sample_value.deserialize_json(item))
    return out
