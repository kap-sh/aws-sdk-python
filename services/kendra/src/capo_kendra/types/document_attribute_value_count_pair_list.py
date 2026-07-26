"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentAttributeValueCountPairList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.document_attribute_value_count_pair

DocumentAttributeValueCountPairList: TypeAlias = list[
    "capo_kendra.types.document_attribute_value_count_pair.DocumentAttributeValueCountPair"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentAttributeValueCountPairList) -> list:
    import capo_kendra.types.document_attribute_value_count_pair

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.document_attribute_value_count_pair.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentAttributeValueCountPairList:
    import capo_kendra.types.document_attribute_value_count_pair

    out: DocumentAttributeValueCountPairList = []
    for item in data:
        out.append(
            capo_kendra.types.document_attribute_value_count_pair.deserialize_aws_json_1_1(
                item
            )
        )
    return out
