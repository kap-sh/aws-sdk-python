"""Generated from Smithy shape ``com.amazonaws.rds#Parameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.apply_method
    import capo_rds.types.boolean
    import capo_rds.types.engine_mode_list
    import capo_rds.types.potentially_sensitive_parameter_value
    import capo_rds.types.string


class Parameter(TypedDict, closed=True):
    parameter_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the parameter.</p>"""
    parameter_value: NotRequired[
        "capo_rds.types.potentially_sensitive_parameter_value.PotentiallySensitiveParameterValue"
    ]
    """<p>The value of the parameter.</p>"""
    description: NotRequired["capo_rds.types.string.String"]
    """<p>Provides a description of the parameter.</p>"""
    source: NotRequired["capo_rds.types.string.String"]
    """<p>The source of the parameter value.</p>"""
    apply_type: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the engine specific parameters type.</p>"""
    data_type: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the valid data type for the parameter.</p>"""
    allowed_values: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the valid range of values for the parameter.</p>"""
    is_modifiable: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether (<code>true</code>) or not (<code>false</code>) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.</p>"""
    minimum_engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The earliest engine version to which the parameter can apply.</p>"""
    apply_method: NotRequired["capo_rds.types.apply_method.ApplyMethod"]
    """<p>Indicates when to apply parameter updates.</p>"""
    supported_engine_modes: NotRequired[
        "capo_rds.types.engine_mode_list.EngineModeList"
    ]
    """<p>The valid DB engine modes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Parameter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "parameter_name" in value:
        pairs.append((f"{key_prefix}ParameterName", str(value["parameter_name"])))
    if "parameter_value" in value:
        pairs.append((f"{key_prefix}ParameterValue", str(value["parameter_value"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "source" in value:
        pairs.append((f"{key_prefix}Source", str(value["source"])))
    if "apply_type" in value:
        pairs.append((f"{key_prefix}ApplyType", str(value["apply_type"])))
    if "data_type" in value:
        pairs.append((f"{key_prefix}DataType", str(value["data_type"])))
    if "allowed_values" in value:
        pairs.append((f"{key_prefix}AllowedValues", str(value["allowed_values"])))
    if "is_modifiable" in value:
        pairs.append(
            (f"{key_prefix}IsModifiable", "true" if value["is_modifiable"] else "false")
        )
    if "minimum_engine_version" in value:
        pairs.append(
            (f"{key_prefix}MinimumEngineVersion", str(value["minimum_engine_version"]))
        )
    if "apply_method" in value:
        import capo_rds.types.apply_method

        capo_rds.types.apply_method.serialize_query(
            value["apply_method"], pairs, f"{key_prefix}ApplyMethod"
        )
    if "supported_engine_modes" in value:
        import capo_rds.types.engine_mode_list

        capo_rds.types.engine_mode_list.serialize_query(
            value["supported_engine_modes"], pairs, f"{key_prefix}SupportedEngineModes"
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
    child_apply_type = el.find("ApplyType")
    if child_apply_type is not None:
        out["apply_type"] = str(child_apply_type.text or "")
    child_data_type = el.find("DataType")
    if child_data_type is not None:
        out["data_type"] = str(child_data_type.text or "")
    child_allowed_values = el.find("AllowedValues")
    if child_allowed_values is not None:
        out["allowed_values"] = str(child_allowed_values.text or "")
    child_is_modifiable = el.find("IsModifiable")
    if child_is_modifiable is not None:
        out["is_modifiable"] = (child_is_modifiable.text or "").lower() == "true"
    child_minimum_engine_version = el.find("MinimumEngineVersion")
    if child_minimum_engine_version is not None:
        out["minimum_engine_version"] = str(child_minimum_engine_version.text or "")
    child_apply_method = el.find("ApplyMethod")
    if child_apply_method is not None:
        import capo_rds.types.apply_method

        out["apply_method"] = capo_rds.types.apply_method.deserialize_query(
            child_apply_method
        )
    child_supported_engine_modes = el.find("SupportedEngineModes")
    if child_supported_engine_modes is not None:
        import capo_rds.types.engine_mode_list

        out["supported_engine_modes"] = (
            capo_rds.types.engine_mode_list.deserialize_query(
                child_supported_engine_modes
            )
        )
    return out
