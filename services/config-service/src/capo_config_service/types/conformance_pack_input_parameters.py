"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackInputParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_input_parameter

ConformancePackInputParameters: TypeAlias = list[
    "capo_config_service.types.conformance_pack_input_parameter.ConformancePackInputParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackInputParameters) -> list:
    import capo_config_service.types.conformance_pack_input_parameter

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.conformance_pack_input_parameter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConformancePackInputParameters:
    import capo_config_service.types.conformance_pack_input_parameter

    out: ConformancePackInputParameters = []
    for item in data:
        out.append(
            capo_config_service.types.conformance_pack_input_parameter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
