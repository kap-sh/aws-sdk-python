"""Generated from Smithy shape ``com.amazonaws.securityhub#ParameterConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.parameter_value
    import aws_sdk_securityhub.types.parameter_value_type


class ParameterConfiguration(TypedDict):
    value_type: NotRequired[
        "aws_sdk_securityhub.types.parameter_value_type.ParameterValueType"
    ]
    """<p> Identifies whether a control parameter uses a custom user-defined value or subscribes to the default Security Hub CSPM behavior.</p> <p>When <code>ValueType</code> is set equal to <code>DEFAULT</code>, the default behavior can be a specific Security Hub CSPM default value, or the default behavior can be to ignore a specific parameter. When <code>ValueType</code> is set equal to <code>DEFAULT</code>, Security Hub CSPM ignores user-provided input for the <code>Value</code> field.</p> <p>When <code>ValueType</code> is set equal to <code>CUSTOM</code>, the <code>Value</code> field can't be empty.</p>"""
    value: NotRequired["aws_sdk_securityhub.types.parameter_value.ParameterValue"]
    """<p> The current value of a control parameter. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterConfiguration) -> dict:
    out: dict = {}
    if "value_type" in value:
        import aws_sdk_securityhub.types.parameter_value_type

        out["ValueType"] = (
            aws_sdk_securityhub.types.parameter_value_type.serialize_json(
                value["value_type"]
            )
        )
    if "value" in value:
        import aws_sdk_securityhub.types.parameter_value

        out["Value"] = aws_sdk_securityhub.types.parameter_value.serialize_json(
            value["value"]
        )
    return out


def deserialize_json(data: dict) -> ParameterConfiguration:
    out: ParameterConfiguration = {}  # type: ignore[typeddict-item]
    if "ValueType" in data:
        import aws_sdk_securityhub.types.parameter_value_type

        out["value_type"] = (
            aws_sdk_securityhub.types.parameter_value_type.deserialize_json(
                data["ValueType"]
            )
        )
    if "Value" in data:
        import aws_sdk_securityhub.types.parameter_value

        out["value"] = aws_sdk_securityhub.types.parameter_value.deserialize_json(
            data["Value"]
        )
    return out
