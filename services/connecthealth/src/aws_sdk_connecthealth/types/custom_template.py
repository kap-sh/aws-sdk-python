"""Generated from Smithy shape ``com.amazonaws.connecthealth#CustomTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.custom_template_base
    import aws_sdk_connecthealth.types.template_instructions


class CustomTemplate(TypedDict, closed=True):
    template_type: "aws_sdk_connecthealth.types.custom_template_base.CustomTemplateBase"
    """<p>The base template type to customize</p>"""
    template_instructions: (
        "aws_sdk_connecthealth.types.template_instructions.TemplateInstructions"
    )
    """<p>Custom instructions for each section of the template</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomTemplate) -> dict:
    out: dict = {}
    import aws_sdk_connecthealth.types.custom_template_base

    out["templateType"] = (
        aws_sdk_connecthealth.types.custom_template_base.serialize_json(
            value["template_type"]
        )
    )
    import aws_sdk_connecthealth.types.template_instructions

    out["templateInstructions"] = (
        aws_sdk_connecthealth.types.template_instructions.serialize_json(
            value["template_instructions"]
        )
    )
    return out


def deserialize_json(data: dict) -> CustomTemplate:
    out: CustomTemplate = {}  # type: ignore[typeddict-item]
    if "templateType" in data:
        import aws_sdk_connecthealth.types.custom_template_base

        out["template_type"] = (
            aws_sdk_connecthealth.types.custom_template_base.deserialize_json(
                data["templateType"]
            )
        )
    else:
        raise DeserializationError("CustomTemplate.template_type required")
    if "templateInstructions" in data:
        import aws_sdk_connecthealth.types.template_instructions

        out["template_instructions"] = (
            aws_sdk_connecthealth.types.template_instructions.deserialize_json(
                data["templateInstructions"]
            )
        )
    else:
        raise DeserializationError("CustomTemplate.template_instructions required")
    return out
