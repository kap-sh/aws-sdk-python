"""Generated from Smithy shape ``com.amazonaws.ssm#SessionManagerParameterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.session_manager_parameter_value

SessionManagerParameterValueList: TypeAlias = list[
    "capo_ssm.types.session_manager_parameter_value.SessionManagerParameterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionManagerParameterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SessionManagerParameterValueList:
    return list(data)
