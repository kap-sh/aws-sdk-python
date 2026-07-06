"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#Entity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.attribute_list
    import aws_sdk_comprehendmedical.types.entity_sub_type
    import aws_sdk_comprehendmedical.types.entity_type
    import aws_sdk_comprehendmedical.types.float
    import aws_sdk_comprehendmedical.types.integer
    import aws_sdk_comprehendmedical.types.string
    import aws_sdk_comprehendmedical.types.trait_list


class Entity(TypedDict, closed=True):
    id: NotRequired["aws_sdk_comprehendmedical.types.integer.Integer"]
    """<p> The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier. </p>"""
    begin_offset: NotRequired["aws_sdk_comprehendmedical.types.integer.Integer"]
    """<p> The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string. </p>"""
    end_offset: NotRequired["aws_sdk_comprehendmedical.types.integer.Integer"]
    """<p> The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string. </p>"""
    score: NotRequired["aws_sdk_comprehendmedical.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend Medical has in the accuracy of the detection.</p>"""
    text: NotRequired["aws_sdk_comprehendmedical.types.string.String"]
    """<p> The segment of input text extracted as this entity.</p>"""
    category: NotRequired["aws_sdk_comprehendmedical.types.entity_type.EntityType"]
    """<p> The category of the entity.</p>"""
    type: NotRequired["aws_sdk_comprehendmedical.types.entity_sub_type.EntitySubType"]
    """<p> Describes the specific type of entity with category of entities.</p>"""
    traits: NotRequired["aws_sdk_comprehendmedical.types.trait_list.TraitList"]
    """<p>Contextual information for the entity.</p>"""
    attributes: NotRequired[
        "aws_sdk_comprehendmedical.types.attribute_list.AttributeList"
    ]
    """<p> The extracted attributes that relate to this entity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Entity) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "score" in value:
        out["Score"] = value["score"]
    if "text" in value:
        out["Text"] = value["text"]
    if "category" in value:
        import aws_sdk_comprehendmedical.types.entity_type

        out["Category"] = (
            aws_sdk_comprehendmedical.types.entity_type.serialize_aws_json_1_1(
                value["category"]
            )
        )
    if "type" in value:
        import aws_sdk_comprehendmedical.types.entity_sub_type

        out["Type"] = (
            aws_sdk_comprehendmedical.types.entity_sub_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "traits" in value:
        import aws_sdk_comprehendmedical.types.trait_list

        out["Traits"] = (
            aws_sdk_comprehendmedical.types.trait_list.serialize_aws_json_1_1(
                value["traits"]
            )
        )
    if "attributes" in value:
        import aws_sdk_comprehendmedical.types.attribute_list

        out["Attributes"] = (
            aws_sdk_comprehendmedical.types.attribute_list.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Entity:
    out: Entity = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "BeginOffset" in data:
        out["begin_offset"] = data["BeginOffset"]
    if "EndOffset" in data:
        out["end_offset"] = data["EndOffset"]
    if "Score" in data:
        out["score"] = data["Score"]
    if "Text" in data:
        out["text"] = data["Text"]
    if "Category" in data:
        import aws_sdk_comprehendmedical.types.entity_type

        out["category"] = (
            aws_sdk_comprehendmedical.types.entity_type.deserialize_aws_json_1_1(
                data["Category"]
            )
        )
    if "Type" in data:
        import aws_sdk_comprehendmedical.types.entity_sub_type

        out["type"] = (
            aws_sdk_comprehendmedical.types.entity_sub_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Traits" in data:
        import aws_sdk_comprehendmedical.types.trait_list

        out["traits"] = (
            aws_sdk_comprehendmedical.types.trait_list.deserialize_aws_json_1_1(
                data["Traits"]
            )
        )
    if "Attributes" in data:
        import aws_sdk_comprehendmedical.types.attribute_list

        out["attributes"] = (
            aws_sdk_comprehendmedical.types.attribute_list.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    return out
