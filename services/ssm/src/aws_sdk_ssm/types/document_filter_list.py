"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_filter

DocumentFilterList: TypeAlias = list["aws_sdk_ssm.types.document_filter.DocumentFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentFilterList) -> list:
    import aws_sdk_ssm.types.document_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.document_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentFilterList:
    import aws_sdk_ssm.types.document_filter

    out: DocumentFilterList = []
    for item in data:
        out.append(aws_sdk_ssm.types.document_filter.deserialize_aws_json_1_1(item))
    return out
