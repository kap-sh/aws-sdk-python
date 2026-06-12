"""Generated from Smithy shape ``com.amazonaws.sagemaker#PropertyNameSuggestion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.resource_property_name


class PropertyNameSuggestion(TypedDict):
    property_name: NotRequired[
        "aws_sdk_sagemaker.types.resource_property_name.ResourcePropertyName"
    ]
    """<p>A suggested property name based on what you entered in the search textbox in the SageMaker console.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PropertyNameSuggestion) -> dict:
    out: dict = {}
    if "property_name" in value:
        out["PropertyName"] = value["property_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PropertyNameSuggestion:
    out: PropertyNameSuggestion = {}  # type: ignore[typeddict-item]
    if "PropertyName" in data:
        out["property_name"] = data["PropertyName"]
    return out
