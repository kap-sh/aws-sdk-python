"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#Attribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.entity_sub_type
    import capo_comprehendmedical.types.entity_type
    import capo_comprehendmedical.types.float
    import capo_comprehendmedical.types.integer
    import capo_comprehendmedical.types.relationship_type
    import capo_comprehendmedical.types.string
    import capo_comprehendmedical.types.trait_list


class Attribute(TypedDict, closed=True):
    type: NotRequired["capo_comprehendmedical.types.entity_sub_type.EntitySubType"]
    """<p> The type of attribute. </p>"""
    score: NotRequired["capo_comprehendmedical.types.float.Float"]
    """<p> The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as an attribute. </p>"""
    relationship_score: NotRequired["capo_comprehendmedical.types.float.Float"]
    """<p> The level of confidence that Amazon Comprehend Medical has that this attribute is correctly related to this entity. </p>"""
    relationship_type: NotRequired[
        "capo_comprehendmedical.types.relationship_type.RelationshipType"
    ]
    """<p>The type of relationship between the entity and attribute. Type for the relationship is <code>OVERLAP</code>, indicating that the entity occurred at the same time as the <code>Date_Expression</code>. </p>"""
    id: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p> The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier. </p>"""
    begin_offset: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p> The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string. </p>"""
    end_offset: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p> The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.</p>"""
    text: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p> The segment of input text extracted as this attribute.</p>"""
    category: NotRequired["capo_comprehendmedical.types.entity_type.EntityType"]
    """<p> The category of attribute. </p>"""
    traits: NotRequired["capo_comprehendmedical.types.trait_list.TraitList"]
    """<p> Contextual information for this attribute. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Attribute) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_comprehendmedical.types.entity_sub_type

        out["Type"] = (
            capo_comprehendmedical.types.entity_sub_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "score" in value:
        out["Score"] = value["score"]
    if "relationship_score" in value:
        out["RelationshipScore"] = value["relationship_score"]
    if "relationship_type" in value:
        import capo_comprehendmedical.types.relationship_type

        out["RelationshipType"] = (
            capo_comprehendmedical.types.relationship_type.serialize_aws_json_1_1(
                value["relationship_type"]
            )
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "text" in value:
        out["Text"] = value["text"]
    if "category" in value:
        import capo_comprehendmedical.types.entity_type

        out["Category"] = (
            capo_comprehendmedical.types.entity_type.serialize_aws_json_1_1(
                value["category"]
            )
        )
    if "traits" in value:
        import capo_comprehendmedical.types.trait_list

        out["Traits"] = capo_comprehendmedical.types.trait_list.serialize_aws_json_1_1(
            value["traits"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Attribute:
    out: Attribute = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_comprehendmedical.types.entity_sub_type

        out["type"] = (
            capo_comprehendmedical.types.entity_sub_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Score" in data:
        out["score"] = data["Score"]
    if "RelationshipScore" in data:
        out["relationship_score"] = data["RelationshipScore"]
    if "RelationshipType" in data:
        import capo_comprehendmedical.types.relationship_type

        out["relationship_type"] = (
            capo_comprehendmedical.types.relationship_type.deserialize_aws_json_1_1(
                data["RelationshipType"]
            )
        )
    if "Id" in data:
        out["id"] = data["Id"]
    if "BeginOffset" in data:
        out["begin_offset"] = data["BeginOffset"]
    if "EndOffset" in data:
        out["end_offset"] = data["EndOffset"]
    if "Text" in data:
        out["text"] = data["Text"]
    if "Category" in data:
        import capo_comprehendmedical.types.entity_type

        out["category"] = (
            capo_comprehendmedical.types.entity_type.deserialize_aws_json_1_1(
                data["Category"]
            )
        )
    if "Traits" in data:
        import capo_comprehendmedical.types.trait_list

        out["traits"] = (
            capo_comprehendmedical.types.trait_list.deserialize_aws_json_1_1(
                data["Traits"]
            )
        )
    return out
