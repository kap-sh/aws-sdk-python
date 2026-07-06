"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.string


class RelationalDatabaseParameter(TypedDict, closed=True):
    allowed_values: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>Specifies the valid range of values for the parameter.</p>"""
    apply_method: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>Indicates when parameter updates are applied.</p> <p>Can be <code>immediate</code> or <code>pending-reboot</code>.</p>"""
    apply_type: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>Specifies the engine-specific parameter type.</p>"""
    data_type: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>Specifies the valid data type for the parameter.</p>"""
    description: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>Provides a description of the parameter.</p>"""
    is_modifiable: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the parameter can be modified.</p>"""
    parameter_name: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>Specifies the name of the parameter.</p>"""
    parameter_value: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>Specifies the value of the parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseParameter) -> dict:
    out: dict = {}
    if "allowed_values" in value:
        out["allowedValues"] = value["allowed_values"]
    if "apply_method" in value:
        out["applyMethod"] = value["apply_method"]
    if "apply_type" in value:
        out["applyType"] = value["apply_type"]
    if "data_type" in value:
        out["dataType"] = value["data_type"]
    if "description" in value:
        out["description"] = value["description"]
    if "is_modifiable" in value:
        out["isModifiable"] = value["is_modifiable"]
    if "parameter_name" in value:
        out["parameterName"] = value["parameter_name"]
    if "parameter_value" in value:
        out["parameterValue"] = value["parameter_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RelationalDatabaseParameter:
    out: RelationalDatabaseParameter = {}  # type: ignore[typeddict-item]
    if "allowedValues" in data:
        out["allowed_values"] = data["allowedValues"]
    if "applyMethod" in data:
        out["apply_method"] = data["applyMethod"]
    if "applyType" in data:
        out["apply_type"] = data["applyType"]
    if "dataType" in data:
        out["data_type"] = data["dataType"]
    if "description" in data:
        out["description"] = data["description"]
    if "isModifiable" in data:
        out["is_modifiable"] = data["isModifiable"]
    if "parameterName" in data:
        out["parameter_name"] = data["parameterName"]
    if "parameterValue" in data:
        out["parameter_value"] = data["parameterValue"]
    return out
