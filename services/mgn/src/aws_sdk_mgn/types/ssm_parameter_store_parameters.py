"""Generated from Smithy shape ``com.amazonaws.mgn#SsmParameterStoreParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.ssm_parameter_store_parameter

SsmParameterStoreParameters: TypeAlias = list[
    "aws_sdk_mgn.types.ssm_parameter_store_parameter.SsmParameterStoreParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SsmParameterStoreParameters) -> list:
    import aws_sdk_mgn.types.ssm_parameter_store_parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_mgn.types.ssm_parameter_store_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SsmParameterStoreParameters:
    import aws_sdk_mgn.types.ssm_parameter_store_parameter

    out: SsmParameterStoreParameters = []
    for item in data:
        out.append(
            aws_sdk_mgn.types.ssm_parameter_store_parameter.deserialize_json(item)
        )
    return out
