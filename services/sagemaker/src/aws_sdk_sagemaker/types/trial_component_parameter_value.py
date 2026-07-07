"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentParameterValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_sagemaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.double_parameter_value
    import aws_sdk_sagemaker.types.string_parameter_value


class _TrialComponentParameterValue_StringValue(TypedDict, closed=True):
    StringValue: "aws_sdk_sagemaker.types.string_parameter_value.StringParameterValue"


class _TrialComponentParameterValue_NumberValue(TypedDict, closed=True):
    NumberValue: "aws_sdk_sagemaker.types.double_parameter_value.DoubleParameterValue"


TrialComponentParameterValue: TypeAlias = (
    _TrialComponentParameterValue_StringValue
    | _TrialComponentParameterValue_NumberValue
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialComponentParameterValue) -> dict:
    if "StringValue" in value:
        return {"StringValue": value["StringValue"]}
    elif "NumberValue" in value:
        return {"NumberValue": value["NumberValue"]}
    else:
        raise SerializationError("TrialComponentParameterValue: no variant present")


def deserialize_aws_json_1_1(data: dict) -> TrialComponentParameterValue:
    if "StringValue" in data:
        return {"StringValue": data["StringValue"]}
    elif "NumberValue" in data:
        return {"NumberValue": data["NumberValue"]}
    else:
        raise DeserializationError(
            "TrialComponentParameterValue: no recognized variant key"
        )
