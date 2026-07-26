"""Generated from Smithy shape ``com.amazonaws.dax#Parameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.change_type
    import capo_dax.types.is_modifiable
    import capo_dax.types.node_type_specific_value_list
    import capo_dax.types.parameter_type
    import capo_dax.types.string


class Parameter(TypedDict, closed=True):
    parameter_name: NotRequired["capo_dax.types.string.String"]
    """<p>The name of the parameter.</p>"""
    parameter_type: NotRequired["capo_dax.types.parameter_type.ParameterType"]
    """<p>Determines whether the parameter can be applied to any nodes, or only nodes of a particular type.</p>"""
    parameter_value: NotRequired["capo_dax.types.string.String"]
    """<p>The value for the parameter.</p>"""
    node_type_specific_values: NotRequired[
        "capo_dax.types.node_type_specific_value_list.NodeTypeSpecificValueList"
    ]
    """<p>A list of node types, and specific parameter values for each node.</p>"""
    description: NotRequired["capo_dax.types.string.String"]
    """<p>A description of the parameter</p>"""
    source: NotRequired["capo_dax.types.string.String"]
    """<p>How the parameter is defined. For example, <code>system</code> denotes a system-defined parameter.</p>"""
    data_type: NotRequired["capo_dax.types.string.String"]
    """<p>The data type of the parameter. For example, <code>integer</code>:</p>"""
    allowed_values: NotRequired["capo_dax.types.string.String"]
    """<p>A range of values within which the parameter can be set.</p>"""
    is_modifiable: NotRequired["capo_dax.types.is_modifiable.IsModifiable"]
    """<p>Whether the customer is allowed to modify the parameter.</p>"""
    change_type: NotRequired["capo_dax.types.change_type.ChangeType"]
    """<p>The conditions under which changes to this parameter can be applied. For example, <code>requires-reboot</code> indicates that a new value for this parameter will only take effect if a node is rebooted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Parameter) -> dict:
    out: dict = {}
    if "parameter_name" in value:
        out["ParameterName"] = value["parameter_name"]
    if "parameter_type" in value:
        import capo_dax.types.parameter_type

        out["ParameterType"] = capo_dax.types.parameter_type.serialize_aws_json_1_1(
            value["parameter_type"]
        )
    if "parameter_value" in value:
        out["ParameterValue"] = value["parameter_value"]
    if "node_type_specific_values" in value:
        import capo_dax.types.node_type_specific_value_list

        out["NodeTypeSpecificValues"] = (
            capo_dax.types.node_type_specific_value_list.serialize_aws_json_1_1(
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
        import capo_dax.types.is_modifiable

        out["IsModifiable"] = capo_dax.types.is_modifiable.serialize_aws_json_1_1(
            value["is_modifiable"]
        )
    if "change_type" in value:
        import capo_dax.types.change_type

        out["ChangeType"] = capo_dax.types.change_type.serialize_aws_json_1_1(
            value["change_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Parameter:
    out: Parameter = {}  # type: ignore[typeddict-item]
    if "ParameterName" in data:
        out["parameter_name"] = data["ParameterName"]
    if "ParameterType" in data:
        import capo_dax.types.parameter_type

        out["parameter_type"] = capo_dax.types.parameter_type.deserialize_aws_json_1_1(
            data["ParameterType"]
        )
    if "ParameterValue" in data:
        out["parameter_value"] = data["ParameterValue"]
    if "NodeTypeSpecificValues" in data:
        import capo_dax.types.node_type_specific_value_list

        out["node_type_specific_values"] = (
            capo_dax.types.node_type_specific_value_list.deserialize_aws_json_1_1(
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
        import capo_dax.types.is_modifiable

        out["is_modifiable"] = capo_dax.types.is_modifiable.deserialize_aws_json_1_1(
            data["IsModifiable"]
        )
    if "ChangeType" in data:
        import capo_dax.types.change_type

        out["change_type"] = capo_dax.types.change_type.deserialize_aws_json_1_1(
            data["ChangeType"]
        )
    return out
