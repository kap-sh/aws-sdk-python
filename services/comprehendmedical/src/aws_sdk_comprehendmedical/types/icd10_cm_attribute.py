"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.float
    import aws_sdk_comprehendmedical.types.icd10_cm_attribute_type
    import aws_sdk_comprehendmedical.types.icd10_cm_entity_type
    import aws_sdk_comprehendmedical.types.icd10_cm_relationship_type
    import aws_sdk_comprehendmedical.types.icd10_cm_trait_list
    import aws_sdk_comprehendmedical.types.integer
    import aws_sdk_comprehendmedical.types.string


class ICD10CMAttribute(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_comprehendmedical.types.icd10_cm_attribute_type.ICD10CMAttributeType"
    ]
    """<p>The type of attribute. InferICD10CM detects entities of the type <code>DX_NAME</code>. </p>"""
    score: NotRequired["aws_sdk_comprehendmedical.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as an attribute.</p>"""
    relationship_score: NotRequired["aws_sdk_comprehendmedical.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend Medical has that this attribute is correctly related to this entity.</p>"""
    id: NotRequired["aws_sdk_comprehendmedical.types.integer.Integer"]
    """<p>The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier.</p>"""
    begin_offset: NotRequired["aws_sdk_comprehendmedical.types.integer.Integer"]
    """<p>The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string.</p>"""
    end_offset: NotRequired["aws_sdk_comprehendmedical.types.integer.Integer"]
    """<p>The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.</p>"""
    text: NotRequired["aws_sdk_comprehendmedical.types.string.String"]
    """<p>The segment of input text which contains the detected attribute.</p>"""
    traits: NotRequired[
        "aws_sdk_comprehendmedical.types.icd10_cm_trait_list.ICD10CMTraitList"
    ]
    """<p>The contextual information for the attribute. The traits recognized by InferICD10CM are <code>DIAGNOSIS</code>, <code>SIGN</code>, <code>SYMPTOM</code>, and <code>NEGATION</code>.</p>"""
    category: NotRequired[
        "aws_sdk_comprehendmedical.types.icd10_cm_entity_type.ICD10CMEntityType"
    ]
    """<p>The category of attribute. Can be either of <code>DX_NAME</code> or <code>TIME_EXPRESSION</code>.</p>"""
    relationship_type: NotRequired[
        "aws_sdk_comprehendmedical.types.icd10_cm_relationship_type.ICD10CMRelationshipType"
    ]
    """<p>The type of relationship between the entity and attribute. Type for the relationship can be either of <code>OVERLAP</code> or <code>SYSTEM_ORGAN_SITE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ICD10CMAttribute) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_comprehendmedical.types.icd10_cm_attribute_type

        out["Type"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_attribute_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "score" in value:
        out["Score"] = value["score"]
    if "relationship_score" in value:
        out["RelationshipScore"] = value["relationship_score"]
    if "id" in value:
        out["Id"] = value["id"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "text" in value:
        out["Text"] = value["text"]
    if "traits" in value:
        import aws_sdk_comprehendmedical.types.icd10_cm_trait_list

        out["Traits"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_trait_list.serialize_aws_json_1_1(
                value["traits"]
            )
        )
    if "category" in value:
        import aws_sdk_comprehendmedical.types.icd10_cm_entity_type

        out["Category"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_entity_type.serialize_aws_json_1_1(
                value["category"]
            )
        )
    if "relationship_type" in value:
        import aws_sdk_comprehendmedical.types.icd10_cm_relationship_type

        out["RelationshipType"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_relationship_type.serialize_aws_json_1_1(
                value["relationship_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ICD10CMAttribute:
    out: ICD10CMAttribute = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_comprehendmedical.types.icd10_cm_attribute_type

        out["type"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_attribute_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Score" in data:
        out["score"] = data["Score"]
    if "RelationshipScore" in data:
        out["relationship_score"] = data["RelationshipScore"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "BeginOffset" in data:
        out["begin_offset"] = data["BeginOffset"]
    if "EndOffset" in data:
        out["end_offset"] = data["EndOffset"]
    if "Text" in data:
        out["text"] = data["Text"]
    if "Traits" in data:
        import aws_sdk_comprehendmedical.types.icd10_cm_trait_list

        out["traits"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_trait_list.deserialize_aws_json_1_1(
                data["Traits"]
            )
        )
    if "Category" in data:
        import aws_sdk_comprehendmedical.types.icd10_cm_entity_type

        out["category"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_entity_type.deserialize_aws_json_1_1(
                data["Category"]
            )
        )
    if "RelationshipType" in data:
        import aws_sdk_comprehendmedical.types.icd10_cm_relationship_type

        out["relationship_type"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_relationship_type.deserialize_aws_json_1_1(
                data["RelationshipType"]
            )
        )
    return out
