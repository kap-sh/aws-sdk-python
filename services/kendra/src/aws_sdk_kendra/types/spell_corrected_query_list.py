"""Generated from Smithy shape ``com.amazonaws.kendra#SpellCorrectedQueryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.spell_corrected_query

SpellCorrectedQueryList: TypeAlias = list[
    "aws_sdk_kendra.types.spell_corrected_query.SpellCorrectedQuery"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpellCorrectedQueryList) -> list:
    import aws_sdk_kendra.types.spell_corrected_query

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.spell_corrected_query.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SpellCorrectedQueryList:
    import aws_sdk_kendra.types.spell_corrected_query

    out: SpellCorrectedQueryList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.spell_corrected_query.deserialize_aws_json_1_1(item)
        )
    return out
