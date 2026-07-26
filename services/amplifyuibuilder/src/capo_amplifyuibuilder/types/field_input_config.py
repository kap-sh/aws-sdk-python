"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FieldInputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.file_uploader_field_config
    import capo_amplifyuibuilder.types.value_mappings


class FieldInputConfig(TypedDict, closed=True):
    type: "str"
    """<p>The input type for the field. </p>"""
    required: NotRequired["bool"]
    """<p>Specifies a field that requires input.</p>"""
    read_only: NotRequired["bool"]
    """<p>Specifies a read only field.</p>"""
    placeholder: NotRequired["str"]
    """<p>The text to display as a placeholder for the field.</p>"""
    default_value: NotRequired["str"]
    """<p>The default value for the field.</p>"""
    descriptive_text: NotRequired["str"]
    """<p>The text to display to describe the field.</p>"""
    default_checked: NotRequired["bool"]
    """<p>Specifies whether a field has a default value.</p>"""
    default_country_code: NotRequired["str"]
    """<p>The default country code for a phone number.</p>"""
    value_mappings: NotRequired[
        "capo_amplifyuibuilder.types.value_mappings.ValueMappings"
    ]
    """<p>The information to use to customize the input fields with data at runtime.</p>"""
    name: NotRequired["str"]
    """<p>The name of the field.</p>"""
    min_value: NotRequired["float"]
    """<p>The minimum value to display for the field.</p>"""
    max_value: NotRequired["float"]
    """<p>The maximum value to display for the field.</p>"""
    step: NotRequired["float"]
    """<p>The stepping increment for a numeric value in a field.</p>"""
    value: NotRequired["str"]
    """<p>The value for the field.</p>"""
    is_array: NotRequired["bool"]
    """<p>Specifies whether to render the field as an array. This property is ignored if the <code>dataSourceType</code> for the form is a Data Store.</p>"""
    file_uploader_config: NotRequired[
        "capo_amplifyuibuilder.types.file_uploader_field_config.FileUploaderFieldConfig"
    ]
    """<p>The configuration for the file uploader field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldInputConfig) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "required" in value:
        out["required"] = value["required"]
    if "read_only" in value:
        out["readOnly"] = value["read_only"]
    if "placeholder" in value:
        out["placeholder"] = value["placeholder"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "descriptive_text" in value:
        out["descriptiveText"] = value["descriptive_text"]
    if "default_checked" in value:
        out["defaultChecked"] = value["default_checked"]
    if "default_country_code" in value:
        out["defaultCountryCode"] = value["default_country_code"]
    if "value_mappings" in value:
        import capo_amplifyuibuilder.types.value_mappings

        out["valueMappings"] = (
            capo_amplifyuibuilder.types.value_mappings.serialize_json(
                value["value_mappings"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "min_value" in value:
        out["minValue"] = value["min_value"]
    if "max_value" in value:
        out["maxValue"] = value["max_value"]
    if "step" in value:
        out["step"] = value["step"]
    if "value" in value:
        out["value"] = value["value"]
    if "is_array" in value:
        out["isArray"] = value["is_array"]
    if "file_uploader_config" in value:
        import capo_amplifyuibuilder.types.file_uploader_field_config

        out["fileUploaderConfig"] = (
            capo_amplifyuibuilder.types.file_uploader_field_config.serialize_json(
                value["file_uploader_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> FieldInputConfig:
    out: FieldInputConfig = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("FieldInputConfig.type required")
    if "required" in data:
        out["required"] = data["required"]
    if "readOnly" in data:
        out["read_only"] = data["readOnly"]
    if "placeholder" in data:
        out["placeholder"] = data["placeholder"]
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    if "descriptiveText" in data:
        out["descriptive_text"] = data["descriptiveText"]
    if "defaultChecked" in data:
        out["default_checked"] = data["defaultChecked"]
    if "defaultCountryCode" in data:
        out["default_country_code"] = data["defaultCountryCode"]
    if "valueMappings" in data:
        import capo_amplifyuibuilder.types.value_mappings

        out["value_mappings"] = (
            capo_amplifyuibuilder.types.value_mappings.deserialize_json(
                data["valueMappings"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "minValue" in data:
        out["min_value"] = data["minValue"]
    if "maxValue" in data:
        out["max_value"] = data["maxValue"]
    if "step" in data:
        out["step"] = data["step"]
    if "value" in data:
        out["value"] = data["value"]
    if "isArray" in data:
        out["is_array"] = data["isArray"]
    if "fileUploaderConfig" in data:
        import capo_amplifyuibuilder.types.file_uploader_field_config

        out["file_uploader_config"] = (
            capo_amplifyuibuilder.types.file_uploader_field_config.deserialize_json(
                data["fileUploaderConfig"]
            )
        )
    return out
