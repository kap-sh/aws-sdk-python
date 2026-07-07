"""Generated from Smithy shape ``com.amazonaws.glue#Option``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.enclosed_in_string_property


class Option(TypedDict, closed=True):
    value: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Specifies the value of the option.</p>"""
    label: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Specifies the label of the option.</p>"""
    description: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Specifies the description of the option.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Option) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "label" in value:
        out["Label"] = value["label"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Option:
    out: Option = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Label" in data:
        out["label"] = data["Label"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
