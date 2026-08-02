"""Generated from Smithy shape ``com.amazonaws.rds#OptionGroupOptionSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.minimum_engine_version_per_allowed_value_list
    import capo_rds.types.string


class OptionGroupOptionSetting(TypedDict, closed=True):
    setting_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the option group option.</p>"""
    setting_description: NotRequired["capo_rds.types.string.String"]
    """<p>The description of the option group option.</p>"""
    default_value: NotRequired["capo_rds.types.string.String"]
    """<p>The default value for the option group option.</p>"""
    apply_type: NotRequired["capo_rds.types.string.String"]
    """<p>The DB engine specific parameter type for the option group option.</p>"""
    allowed_values: NotRequired["capo_rds.types.string.String"]
    """<p>Indicates the acceptable values for the option group option.</p>"""
    is_modifiable: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether this option group option can be changed from the default value.</p>"""
    is_required: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether a value must be specified for this option setting of the option group option.</p>"""
    minimum_engine_version_per_allowed_value: NotRequired[
        "capo_rds.types.minimum_engine_version_per_allowed_value_list.MinimumEngineVersionPerAllowedValueList"
    ]
    """<p>The minimum DB engine version required for the corresponding allowed value for this option setting.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionGroupOptionSetting, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "setting_name" in value:
        pairs.append((f"{key_prefix}SettingName", str(value["setting_name"])))
    if "setting_description" in value:
        pairs.append(
            (f"{key_prefix}SettingDescription", str(value["setting_description"]))
        )
    if "default_value" in value:
        pairs.append((f"{key_prefix}DefaultValue", str(value["default_value"])))
    if "apply_type" in value:
        pairs.append((f"{key_prefix}ApplyType", str(value["apply_type"])))
    if "allowed_values" in value:
        pairs.append((f"{key_prefix}AllowedValues", str(value["allowed_values"])))
    if "is_modifiable" in value:
        pairs.append(
            (f"{key_prefix}IsModifiable", "true" if value["is_modifiable"] else "false")
        )
    if "is_required" in value:
        pairs.append(
            (f"{key_prefix}IsRequired", "true" if value["is_required"] else "false")
        )
    if "minimum_engine_version_per_allowed_value" in value:
        import capo_rds.types.minimum_engine_version_per_allowed_value_list

        capo_rds.types.minimum_engine_version_per_allowed_value_list.serialize_query(
            value["minimum_engine_version_per_allowed_value"],
            pairs,
            f"{key_prefix}MinimumEngineVersionPerAllowedValue",
        )


def deserialize_query(el: Element) -> OptionGroupOptionSetting:
    out: OptionGroupOptionSetting = {}  # type: ignore[typeddict-item]
    child_setting_name = el.find("SettingName")
    if child_setting_name is not None:
        out["setting_name"] = str(child_setting_name.text or "")
    child_setting_description = el.find("SettingDescription")
    if child_setting_description is not None:
        out["setting_description"] = str(child_setting_description.text or "")
    child_default_value = el.find("DefaultValue")
    if child_default_value is not None:
        out["default_value"] = str(child_default_value.text or "")
    child_apply_type = el.find("ApplyType")
    if child_apply_type is not None:
        out["apply_type"] = str(child_apply_type.text or "")
    child_allowed_values = el.find("AllowedValues")
    if child_allowed_values is not None:
        out["allowed_values"] = str(child_allowed_values.text or "")
    child_is_modifiable = el.find("IsModifiable")
    if child_is_modifiable is not None:
        out["is_modifiable"] = (child_is_modifiable.text or "").lower() == "true"
    child_is_required = el.find("IsRequired")
    if child_is_required is not None:
        out["is_required"] = (child_is_required.text or "").lower() == "true"
    child_minimum_engine_version_per_allowed_value = el.find(
        "MinimumEngineVersionPerAllowedValue"
    )
    if child_minimum_engine_version_per_allowed_value is not None:
        import capo_rds.types.minimum_engine_version_per_allowed_value_list

        out["minimum_engine_version_per_allowed_value"] = (
            capo_rds.types.minimum_engine_version_per_allowed_value_list.deserialize_query(
                child_minimum_engine_version_per_allowed_value
            )
        )
    return out
