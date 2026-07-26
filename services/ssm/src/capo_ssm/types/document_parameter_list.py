"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.document_parameter

DocumentParameterList: TypeAlias = list[
    "capo_ssm.types.document_parameter.DocumentParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentParameterList) -> list:
    import capo_ssm.types.document_parameter

    out: list = []
    for item in value:
        out.append(capo_ssm.types.document_parameter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentParameterList:
    import capo_ssm.types.document_parameter

    out: DocumentParameterList = []
    for item in data:
        out.append(capo_ssm.types.document_parameter.deserialize_aws_json_1_1(item))
    return out
