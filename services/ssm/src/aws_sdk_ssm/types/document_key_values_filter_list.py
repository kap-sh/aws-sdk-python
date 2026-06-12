"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentKeyValuesFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_key_values_filter

DocumentKeyValuesFilterList: TypeAlias = list[
    "aws_sdk_ssm.types.document_key_values_filter.DocumentKeyValuesFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentKeyValuesFilterList) -> list:
    import aws_sdk_ssm.types.document_key_values_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.document_key_values_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentKeyValuesFilterList:
    import aws_sdk_ssm.types.document_key_values_filter

    out: DocumentKeyValuesFilterList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.document_key_values_filter.deserialize_aws_json_1_1(item)
        )
    return out
