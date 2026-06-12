"""Generated from Smithy shape ``com.amazonaws.panorama#TemplateParametersMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_panorama.types.template_key
    import aws_sdk_panorama.types.template_value

TemplateParametersMap: TypeAlias = dict[
    "aws_sdk_panorama.types.template_key.TemplateKey",
    "aws_sdk_panorama.types.template_value.TemplateValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TemplateParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TemplateParametersMap:
    out: TemplateParametersMap = {}
    for key, value in data.items():
        out[key] = value
    return out
