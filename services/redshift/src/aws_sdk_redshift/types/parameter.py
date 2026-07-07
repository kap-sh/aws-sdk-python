"""Generated from Smithy shape ``com.amazonaws.redshift#Parameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.boolean
    import aws_sdk_redshift.types.parameter_apply_type
    import aws_sdk_redshift.types.string


class Parameter(TypedDict, closed=True):
    parameter_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the parameter.</p>"""
    parameter_value: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The value of the parameter. If <code>ParameterName</code> is <code>wlm_json_configuration</code>, then the maximum size of <code>ParameterValue</code> is 8000 characters.</p>"""
    description: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A description of the parameter.</p>"""
    source: NotRequired["aws_sdk_redshift.types.string.String"]
    r"""<p>The source of the parameter value, such as \"engine-default\" or \"user\".</p>"""
    data_type: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The data type of the parameter.</p>"""
    allowed_values: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The valid range of values for the parameter.</p>"""
    apply_type: NotRequired[
        "aws_sdk_redshift.types.parameter_apply_type.ParameterApplyType"
    ]
    r"""<p>Specifies how to apply the WLM configuration parameter. Some properties can be applied dynamically, while other properties require that any associated clusters be rebooted for the configuration changes to be applied. For more information about parameters and parameter groups, go to <a href=\"https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html\">Amazon Redshift Parameter Groups</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>"""
    is_modifiable: NotRequired["aws_sdk_redshift.types.boolean.Boolean"]
    """<p>If <code>true</code>, the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed. </p>"""
    minimum_engine_version: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The earliest engine version to which the parameter can apply.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Parameter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "parameter_name" in value:
        pairs.append((f"{prefix}.ParameterName", str(value["parameter_name"])))
    if "parameter_value" in value:
        pairs.append((f"{prefix}.ParameterValue", str(value["parameter_value"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "source" in value:
        pairs.append((f"{prefix}.Source", str(value["source"])))
    if "data_type" in value:
        pairs.append((f"{prefix}.DataType", str(value["data_type"])))
    if "allowed_values" in value:
        pairs.append((f"{prefix}.AllowedValues", str(value["allowed_values"])))
    if "apply_type" in value:
        import aws_sdk_redshift.types.parameter_apply_type

        aws_sdk_redshift.types.parameter_apply_type.serialize_query(
            value["apply_type"], pairs, f"{prefix}.ApplyType"
        )
    if "is_modifiable" in value:
        pairs.append(
            (f"{prefix}.IsModifiable", "true" if value["is_modifiable"] else "false")
        )
    if "minimum_engine_version" in value:
        pairs.append(
            (f"{prefix}.MinimumEngineVersion", str(value["minimum_engine_version"]))
        )


def deserialize_query(el: Element) -> Parameter:
    out: Parameter = {}  # type: ignore[typeddict-item]
    child_parameter_name = el.find("ParameterName")
    if child_parameter_name is not None:
        out["parameter_name"] = str(child_parameter_name.text or "")
    child_parameter_value = el.find("ParameterValue")
    if child_parameter_value is not None:
        out["parameter_value"] = str(child_parameter_value.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_source = el.find("Source")
    if child_source is not None:
        out["source"] = str(child_source.text or "")
    child_data_type = el.find("DataType")
    if child_data_type is not None:
        out["data_type"] = str(child_data_type.text or "")
    child_allowed_values = el.find("AllowedValues")
    if child_allowed_values is not None:
        out["allowed_values"] = str(child_allowed_values.text or "")
    child_apply_type = el.find("ApplyType")
    if child_apply_type is not None:
        import aws_sdk_redshift.types.parameter_apply_type

        out["apply_type"] = (
            aws_sdk_redshift.types.parameter_apply_type.deserialize_query(
                child_apply_type
            )
        )
    child_is_modifiable = el.find("IsModifiable")
    if child_is_modifiable is not None:
        out["is_modifiable"] = (child_is_modifiable.text or "").lower() == "true"
    child_minimum_engine_version = el.find("MinimumEngineVersion")
    if child_minimum_engine_version is not None:
        out["minimum_engine_version"] = str(child_minimum_engine_version.text or "")
    return out
