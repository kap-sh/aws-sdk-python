"""Generated from Smithy shape ``com.amazonaws.sagemaker#PropertyNameQuery``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.property_name_hint


class PropertyNameQuery(TypedDict):
    property_name_hint: NotRequired[
        "aws_sdk_sagemaker.types.property_name_hint.PropertyNameHint"
    ]
    """<p>Text that begins a property's name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PropertyNameQuery) -> dict:
    out: dict = {}
    if "property_name_hint" in value:
        out["PropertyNameHint"] = value["property_name_hint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PropertyNameQuery:
    out: PropertyNameQuery = {}  # type: ignore[typeddict-item]
    if "PropertyNameHint" in data:
        out["property_name_hint"] = data["PropertyNameHint"]
    return out
