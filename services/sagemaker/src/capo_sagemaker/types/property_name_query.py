"""Generated from Smithy shape ``com.amazonaws.sagemaker#PropertyNameQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.property_name_hint


class PropertyNameQuery(TypedDict, closed=True):
    property_name_hint: NotRequired[
        "capo_sagemaker.types.property_name_hint.PropertyNameHint"
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
