"""Generated from Smithy shape ``com.amazonaws.kendra#SuggestableConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.document_attribute_key
    import aws_sdk_kendra.types.object_boolean


class SuggestableConfig(TypedDict):
    attribute_name: NotRequired[
        "aws_sdk_kendra.types.document_attribute_key.DocumentAttributeKey"
    ]
    """<p>The name of the document field/attribute.</p>"""
    suggestable: NotRequired["aws_sdk_kendra.types.object_boolean.ObjectBoolean"]
    """<p> <code>TRUE</code> means the document field/attribute is suggestible, so the contents within the field can be used for query suggestions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuggestableConfig) -> dict:
    out: dict = {}
    if "attribute_name" in value:
        out["AttributeName"] = value["attribute_name"]
    if "suggestable" in value:
        out["Suggestable"] = value["suggestable"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SuggestableConfig:
    out: SuggestableConfig = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    if "Suggestable" in data:
        out["suggestable"] = data["Suggestable"]
    return out
