"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityTypesListItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.entity_type_name


class EntityTypesListItem(TypedDict):
    type: "aws_sdk_comprehend.types.entity_type_name.EntityTypeName"
    r"""<p>An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer.</p> <p>Entity types must not contain the following invalid characters: \n (line break), \\n (escaped line break, \r (carriage return), \\r (escaped carriage return), \t (tab), \\t (escaped tab), and , (comma).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityTypesListItem) -> dict:
    out: dict = {}
    out["Type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityTypesListItem:
    out: EntityTypesListItem = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("EntityTypesListItem.type required")
    return out
