"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.entity_description
    import aws_sdk_sagemaker.types.hyper_parameter_value
    import aws_sdk_sagemaker.types.parameter_name
    import aws_sdk_sagemaker.types.parameter_range
    import aws_sdk_sagemaker.types.parameter_type


class HyperParameterSpecification(TypedDict, closed=True):
    name: NotRequired["aws_sdk_sagemaker.types.parameter_name.ParameterName"]
    """<p>The name of this hyperparameter. The name must be unique.</p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>A brief description of the hyperparameter.</p>"""
    type: NotRequired["aws_sdk_sagemaker.types.parameter_type.ParameterType"]
    """<p>The type of this hyperparameter. The valid types are <code>Integer</code>, <code>Continuous</code>, <code>Categorical</code>, and <code>FreeText</code>.</p>"""
    range: NotRequired["aws_sdk_sagemaker.types.parameter_range.ParameterRange"]
    """<p>The allowed range for this hyperparameter.</p>"""
    is_tunable: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>Indicates whether this hyperparameter is tunable in a hyperparameter tuning job.</p>"""
    is_required: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>Indicates whether this hyperparameter is required.</p>"""
    default_value: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_value.HyperParameterValue"
    ]
    """<p>The default value for this hyperparameter. If a default value is specified, a hyperparameter cannot be required.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterSpecification) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import aws_sdk_sagemaker.types.parameter_type

        out["Type"] = aws_sdk_sagemaker.types.parameter_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "range" in value:
        import aws_sdk_sagemaker.types.parameter_range

        out["Range"] = aws_sdk_sagemaker.types.parameter_range.serialize_aws_json_1_1(
            value["range"]
        )
    if "is_tunable" in value:
        out["IsTunable"] = value["is_tunable"]
    if "is_required" in value:
        out["IsRequired"] = value["is_required"]
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameterSpecification:
    out: HyperParameterSpecification = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Type" in data:
        import aws_sdk_sagemaker.types.parameter_type

        out["type"] = aws_sdk_sagemaker.types.parameter_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Range" in data:
        import aws_sdk_sagemaker.types.parameter_range

        out["range"] = aws_sdk_sagemaker.types.parameter_range.deserialize_aws_json_1_1(
            data["Range"]
        )
    if "IsTunable" in data:
        out["is_tunable"] = data["IsTunable"]
    if "IsRequired" in data:
        out["is_required"] = data["IsRequired"]
    if "DefaultValue" in data:
        out["default_value"] = data["DefaultValue"]
    return out
