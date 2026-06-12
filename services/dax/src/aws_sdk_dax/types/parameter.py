"""Generated from Smithy shape ``com.amazonaws.dax#Parameter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dax.types.change_type
    import aws_sdk_dax.types.is_modifiable
    import aws_sdk_dax.types.node_type_specific_value_list
    import aws_sdk_dax.types.parameter_type
    import aws_sdk_dax.types.string


class Parameter(TypedDict):
    parameter_name: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>The name of the parameter.</p>"""
    parameter_type: NotRequired["aws_sdk_dax.types.parameter_type.ParameterType"]
    """<p>Determines whether the parameter can be applied to any nodes, or only nodes of a particular type.</p>"""
    parameter_value: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>The value for the parameter.</p>"""
    node_type_specific_values: NotRequired[
        "aws_sdk_dax.types.node_type_specific_value_list.NodeTypeSpecificValueList"
    ]
    """<p>A list of node types, and specific parameter values for each node.</p>"""
    description: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>A description of the parameter</p>"""
    source: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>How the parameter is defined. For example, <code>system</code> denotes a system-defined parameter.</p>"""
    data_type: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>The data type of the parameter. For example, <code>integer</code>:</p>"""
    allowed_values: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>A range of values within which the parameter can be set.</p>"""
    is_modifiable: NotRequired["aws_sdk_dax.types.is_modifiable.IsModifiable"]
    """<p>Whether the customer is allowed to modify the parameter.</p>"""
    change_type: NotRequired["aws_sdk_dax.types.change_type.ChangeType"]
    """<p>The conditions under which changes to this parameter can be applied. For example, <code>requires-reboot</code> indicates that a new value for this parameter will only take effect if a node is rebooted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Parameter) -> dict:
    out: dict = {}
    if "parameter_name" in value:
        out["ParameterName"] = value["parameter_name"]
    if "parameter_type" in value:
        import aws_sdk_dax.types.parameter_type

        out["ParameterType"] = aws_sdk_dax.types.parameter_type.serialize_aws_json_1_1(
            value["parameter_type"]
        )
    if "parameter_value" in value:
        out["ParameterValue"] = value["parameter_value"]
    if "node_type_specific_values" in value:
        import aws_sdk_dax.types.node_type_specific_value_list

        out["NodeTypeSpecificValues"] = (
            aws_sdk_dax.types.node_type_specific_value_list.serialize_aws_json_1_1(
                value["node_type_specific_values"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "source" in value:
        out["Source"] = value["source"]
    if "data_type" in value:
        out["DataType"] = value["data_type"]
    if "allowed_values" in value:
        out["AllowedValues"] = value["allowed_values"]
    if "is_modifiable" in value:
        import aws_sdk_dax.types.is_modifiable

        out["IsModifiable"] = aws_sdk_dax.types.is_modifiable.serialize_aws_json_1_1(
            value["is_modifiable"]
        )
    if "change_type" in value:
        import aws_sdk_dax.types.change_type

        out["ChangeType"] = aws_sdk_dax.types.change_type.serialize_aws_json_1_1(
            value["change_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Parameter:
    out: Parameter = {}  # type: ignore[typeddict-item]
    if "ParameterName" in data:
        out["parameter_name"] = data["ParameterName"]
    if "ParameterType" in data:
        import aws_sdk_dax.types.parameter_type

        out["parameter_type"] = (
            aws_sdk_dax.types.parameter_type.deserialize_aws_json_1_1(
                data["ParameterType"]
            )
        )
    if "ParameterValue" in data:
        out["parameter_value"] = data["ParameterValue"]
    if "NodeTypeSpecificValues" in data:
        import aws_sdk_dax.types.node_type_specific_value_list

        out["node_type_specific_values"] = (
            aws_sdk_dax.types.node_type_specific_value_list.deserialize_aws_json_1_1(
                data["NodeTypeSpecificValues"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Source" in data:
        out["source"] = data["Source"]
    if "DataType" in data:
        out["data_type"] = data["DataType"]
    if "AllowedValues" in data:
        out["allowed_values"] = data["AllowedValues"]
    if "IsModifiable" in data:
        import aws_sdk_dax.types.is_modifiable

        out["is_modifiable"] = aws_sdk_dax.types.is_modifiable.deserialize_aws_json_1_1(
            data["IsModifiable"]
        )
    if "ChangeType" in data:
        import aws_sdk_dax.types.change_type

        out["change_type"] = aws_sdk_dax.types.change_type.deserialize_aws_json_1_1(
            data["ChangeType"]
        )
    return out
