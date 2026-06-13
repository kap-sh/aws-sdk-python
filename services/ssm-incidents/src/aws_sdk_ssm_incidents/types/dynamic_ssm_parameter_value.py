"""Generated from Smithy shape ``com.amazonaws.ssmincidents#DynamicSsmParameterValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.variable_type


class _DynamicSsmParameterValue_variable(TypedDict):
    variable: "aws_sdk_ssm_incidents.types.variable_type.VariableType"


DynamicSsmParameterValue: TypeAlias = _DynamicSsmParameterValue_variable


# --- restJson1 ser/de ---
def serialize_json(value: DynamicSsmParameterValue) -> dict:
    if "variable" in value:
        return {"variable": value["variable"]}
    else:
        raise SerializationError("DynamicSsmParameterValue: no variant present")


def deserialize_json(data: dict) -> DynamicSsmParameterValue:
    if "variable" in data:
        return {"variable": data["variable"]}
    else:
        raise DeserializationError(
            "DynamicSsmParameterValue: no recognized variant key"
        )
