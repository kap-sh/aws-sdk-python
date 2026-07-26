"""Generated from Smithy shape ``com.amazonaws.neptune#Parameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.apply_method
    import capo_neptune.types.boolean
    import capo_neptune.types.string


class Parameter(TypedDict, closed=True):
    parameter_name: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the name of the parameter.</p>"""
    parameter_value: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the value of the parameter.</p>"""
    description: NotRequired["capo_neptune.types.string.String"]
    """<p>Provides a description of the parameter.</p>"""
    source: NotRequired["capo_neptune.types.string.String"]
    """<p>Indicates the source of the parameter value.</p>"""
    apply_type: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the engine specific parameters type.</p>"""
    data_type: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the valid data type for the parameter.</p>"""
    allowed_values: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the valid range of values for the parameter.</p>"""
    is_modifiable: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p> Indicates whether (<code>true</code>) or not (<code>false</code>) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.</p>"""
    minimum_engine_version: NotRequired["capo_neptune.types.string.String"]
    """<p>The earliest engine version to which the parameter can apply.</p>"""
    apply_method: NotRequired["capo_neptune.types.apply_method.ApplyMethod"]
    """<p>Indicates when to apply parameter updates.</p>"""


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
    if "apply_type" in value:
        pairs.append((f"{prefix}.ApplyType", str(value["apply_type"])))
    if "data_type" in value:
        pairs.append((f"{prefix}.DataType", str(value["data_type"])))
    if "allowed_values" in value:
        pairs.append((f"{prefix}.AllowedValues", str(value["allowed_values"])))
    if "is_modifiable" in value:
        pairs.append(
            (f"{prefix}.IsModifiable", "true" if value["is_modifiable"] else "false")
        )
    if "minimum_engine_version" in value:
        pairs.append(
            (f"{prefix}.MinimumEngineVersion", str(value["minimum_engine_version"]))
        )
    if "apply_method" in value:
        import capo_neptune.types.apply_method

        capo_neptune.types.apply_method.serialize_query(
            value["apply_method"], pairs, f"{prefix}.ApplyMethod"
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
        import capo_neptune.types.apply_method

        out["apply_method"] = capo_neptune.types.apply_method.deserialize_query(
            child_apply_method
        )
    return out
