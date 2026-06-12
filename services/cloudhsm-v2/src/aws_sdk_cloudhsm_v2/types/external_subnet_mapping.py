"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#ExternalSubnetMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.external_az
    import aws_sdk_cloudhsm_v2.types.subnet_id

ExternalSubnetMapping: TypeAlias = dict[
    "aws_sdk_cloudhsm_v2.types.external_az.ExternalAz",
    "aws_sdk_cloudhsm_v2.types.subnet_id.SubnetId",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ExternalSubnetMapping) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ExternalSubnetMapping:
    out: ExternalSubnetMapping = {}
    for key, value in data.items():
        out[key] = value
    return out
