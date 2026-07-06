"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateSourceTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn


class TemplateSourceTemplate(TypedDict, closed=True):
    arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSourceTemplate) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> TemplateSourceTemplate:
    out: TemplateSourceTemplate = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("TemplateSourceTemplate.arn required")
    return out
