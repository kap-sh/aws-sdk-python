"""Generated from Smithy shape ``com.amazonaws.mgn#SsmDocumentExternalParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.ssm_document_parameter_name
    import aws_sdk_mgn.types.ssm_external_parameter

SsmDocumentExternalParameters: TypeAlias = dict[
    "aws_sdk_mgn.types.ssm_document_parameter_name.SsmDocumentParameterName",
    "aws_sdk_mgn.types.ssm_external_parameter.SsmExternalParameter",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SsmDocumentExternalParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_mgn.types.ssm_external_parameter

        out[key] = aws_sdk_mgn.types.ssm_external_parameter.serialize_json(value)
    return out


def deserialize_json(data: dict) -> SsmDocumentExternalParameters:
    out: SsmDocumentExternalParameters = {}
    for key, value in data.items():
        import aws_sdk_mgn.types.ssm_external_parameter

        out[key] = aws_sdk_mgn.types.ssm_external_parameter.deserialize_json(value)
    return out
