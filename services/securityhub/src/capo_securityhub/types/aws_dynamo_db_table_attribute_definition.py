"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableAttributeDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsDynamoDbTableAttributeDefinition(TypedDict, closed=True):
    attribute_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the attribute.</p>"""
    attribute_type: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The type of the attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableAttributeDefinition) -> dict:
    out: dict = {}
    if "attribute_name" in value:
        out["AttributeName"] = value["attribute_name"]
    if "attribute_type" in value:
        out["AttributeType"] = value["attribute_type"]
    return out


def deserialize_json(data: dict) -> AwsDynamoDbTableAttributeDefinition:
    out: AwsDynamoDbTableAttributeDefinition = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    if "AttributeType" in data:
        out["attribute_type"] = data["AttributeType"]
    return out
