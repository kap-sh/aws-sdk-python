"""Generated from Smithy shape ``com.amazonaws.connecthealth#CustomTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.custom_template_base


class CustomTemplateResponse(TypedDict):
    template_type: NotRequired[
        "aws_sdk_connecthealth.types.custom_template_base.CustomTemplateBase"
    ]
    """<p>The base template type that was customized</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomTemplateResponse) -> dict:
    out: dict = {}
    if "template_type" in value:
        import aws_sdk_connecthealth.types.custom_template_base

        out["templateType"] = (
            aws_sdk_connecthealth.types.custom_template_base.serialize_json(
                value["template_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomTemplateResponse:
    out: CustomTemplateResponse = {}  # type: ignore[typeddict-item]
    if "templateType" in data:
        import aws_sdk_connecthealth.types.custom_template_base

        out["template_type"] = (
            aws_sdk_connecthealth.types.custom_template_base.deserialize_json(
                data["templateType"]
            )
        )
    return out
