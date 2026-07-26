"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FieldConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.field_input_config
    import capo_amplifyuibuilder.types.field_position
    import capo_amplifyuibuilder.types.validations_list


class FieldConfig(TypedDict, closed=True):
    label: NotRequired["str"]
    """<p>The label for the field.</p>"""
    position: NotRequired["capo_amplifyuibuilder.types.field_position.FieldPosition"]
    """<p>Specifies the field position.</p>"""
    excluded: NotRequired["bool"]
    """<p>Specifies whether to hide a field.</p>"""
    input_type: NotRequired[
        "capo_amplifyuibuilder.types.field_input_config.FieldInputConfig"
    ]
    """<p>Describes the configuration for the default input value to display for a field.</p>"""
    validations: NotRequired[
        "capo_amplifyuibuilder.types.validations_list.ValidationsList"
    ]
    """<p>The validations to perform on the value in the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldConfig) -> dict:
    out: dict = {}
    if "label" in value:
        out["label"] = value["label"]
    if "position" in value:
        import capo_amplifyuibuilder.types.field_position

        out["position"] = capo_amplifyuibuilder.types.field_position.serialize_json(
            value["position"]
        )
    if "excluded" in value:
        out["excluded"] = value["excluded"]
    if "input_type" in value:
        import capo_amplifyuibuilder.types.field_input_config

        out["inputType"] = (
            capo_amplifyuibuilder.types.field_input_config.serialize_json(
                value["input_type"]
            )
        )
    if "validations" in value:
        import capo_amplifyuibuilder.types.validations_list

        out["validations"] = (
            capo_amplifyuibuilder.types.validations_list.serialize_json(
                value["validations"]
            )
        )
    return out


def deserialize_json(data: dict) -> FieldConfig:
    out: FieldConfig = {}  # type: ignore[typeddict-item]
    if "label" in data:
        out["label"] = data["label"]
    if "position" in data:
        import capo_amplifyuibuilder.types.field_position

        out["position"] = capo_amplifyuibuilder.types.field_position.deserialize_json(
            data["position"]
        )
    if "excluded" in data:
        out["excluded"] = data["excluded"]
    if "inputType" in data:
        import capo_amplifyuibuilder.types.field_input_config

        out["input_type"] = (
            capo_amplifyuibuilder.types.field_input_config.deserialize_json(
                data["inputType"]
            )
        )
    if "validations" in data:
        import capo_amplifyuibuilder.types.validations_list

        out["validations"] = (
            capo_amplifyuibuilder.types.validations_list.deserialize_json(
                data["validations"]
            )
        )
    return out
