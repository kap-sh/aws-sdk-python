"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentKeyValuesFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.document_key_values_filter

DocumentKeyValuesFilterList: TypeAlias = list[
    "capo_ssm.types.document_key_values_filter.DocumentKeyValuesFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentKeyValuesFilterList) -> list:
    import capo_ssm.types.document_key_values_filter

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.document_key_values_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentKeyValuesFilterList:
    import capo_ssm.types.document_key_values_filter

    out: DocumentKeyValuesFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ssm.types.document_key_values_filter.deserialize_aws_json_1_1(item)
        )
    return out
