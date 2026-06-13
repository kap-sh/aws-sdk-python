"""Generated from Smithy shape ``com.amazonaws.mgn#SsmDocumentParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.ssm_document_parameter_name
    import aws_sdk_mgn.types.ssm_parameter_store_parameters

SsmDocumentParameters: TypeAlias = dict[
    "aws_sdk_mgn.types.ssm_document_parameter_name.SsmDocumentParameterName",
    "aws_sdk_mgn.types.ssm_parameter_store_parameters.SsmParameterStoreParameters",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SsmDocumentParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_mgn.types.ssm_parameter_store_parameters

        out[key] = aws_sdk_mgn.types.ssm_parameter_store_parameters.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> SsmDocumentParameters:
    out: SsmDocumentParameters = {}
    for key, value in data.items():
        import aws_sdk_mgn.types.ssm_parameter_store_parameters

        out[key] = aws_sdk_mgn.types.ssm_parameter_store_parameters.deserialize_json(
            value
        )
    return out
