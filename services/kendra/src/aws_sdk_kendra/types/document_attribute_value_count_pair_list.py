"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentAttributeValueCountPairList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.document_attribute_value_count_pair

DocumentAttributeValueCountPairList: TypeAlias = list[
    "aws_sdk_kendra.types.document_attribute_value_count_pair.DocumentAttributeValueCountPair"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentAttributeValueCountPairList) -> list:
    import aws_sdk_kendra.types.document_attribute_value_count_pair

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.document_attribute_value_count_pair.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentAttributeValueCountPairList:
    import aws_sdk_kendra.types.document_attribute_value_count_pair

    out: DocumentAttributeValueCountPairList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.document_attribute_value_count_pair.deserialize_aws_json_1_1(
                item
            )
        )
    return out
