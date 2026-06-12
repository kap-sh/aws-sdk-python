"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMEntity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.float
    import aws_sdk_comprehendmedical.types.icd10_cm_attribute_list
    import aws_sdk_comprehendmedical.types.icd10_cm_concept_list
    import aws_sdk_comprehendmedical.types.icd10_cm_entity_category
    import aws_sdk_comprehendmedical.types.icd10_cm_entity_type
    import aws_sdk_comprehendmedical.types.icd10_cm_trait_list
    import aws_sdk_comprehendmedical.types.integer
    import aws_sdk_comprehendmedical.types.ontology_linking_bounded_length_string


class ICD10CMEntity(TypedDict):
    id: NotRequired["aws_sdk_comprehendmedical.types.integer.Integer"]
    """<p>The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier.</p>"""
    text: NotRequired[
        "aws_sdk_comprehendmedical.types.ontology_linking_bounded_length_string.OntologyLinkingBoundedLengthString"
    ]
    """<p>The segment of input text that is matched to the detected entity.</p>"""
    category: NotRequired[
        "aws_sdk_comprehendmedical.types.icd10_cm_entity_category.ICD10CMEntityCategory"
    ]
    """<p> The category of the entity. InferICD10CM detects entities in the <code>MEDICAL_CONDITION</code> category. </p>"""
    type: NotRequired[
        "aws_sdk_comprehendmedical.types.icd10_cm_entity_type.ICD10CMEntityType"
    ]
    """<p>Describes the specific type of entity with category of entities. InferICD10CM detects entities of the type <code>DX_NAME</code> and <code>TIME_EXPRESSION</code>.</p>"""
    score: NotRequired["aws_sdk_comprehendmedical.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend Medical has in the accuracy of the detection.</p>"""
    begin_offset: NotRequired["aws_sdk_comprehendmedical.types.integer.Integer"]
    """<p>The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string.</p>"""
    end_offset: NotRequired["aws_sdk_comprehendmedical.types.integer.Integer"]
    """<p>The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string.</p>"""
    attributes: NotRequired[
        "aws_sdk_comprehendmedical.types.icd10_cm_attribute_list.ICD10CMAttributeList"
    ]
    """<p>The detected attributes that relate to the entity. An extracted segment of the text that is an attribute of an entity, or otherwise related to an entity, such as the nature of a medical condition.</p>"""
    traits: NotRequired[
        "aws_sdk_comprehendmedical.types.icd10_cm_trait_list.ICD10CMTraitList"
    ]
    """<p>Provides Contextual information for the entity. The traits recognized by InferICD10CM are <code>DIAGNOSIS</code>, <code>SIGN</code>, <code>SYMPTOM</code>, and <code>NEGATION.</code> </p>"""
    icd10_cm_concepts: NotRequired[
        "aws_sdk_comprehendmedical.types.icd10_cm_concept_list.ICD10CMConceptList"
    ]
    """<p>The ICD-10-CM concepts that the entity could refer to, along with a score indicating the likelihood of the match.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ICD10CMEntity) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "text" in value:
        out["Text"] = value["text"]
    if "category" in value:
        import aws_sdk_comprehendmedical.types.icd10_cm_entity_category

        out["Category"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_entity_category.serialize_aws_json_1_1(
                value["category"]
            )
        )
    if "type" in value:
        import aws_sdk_comprehendmedical.types.icd10_cm_entity_type

        out["Type"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_entity_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "score" in value:
        out["Score"] = value["score"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "attributes" in value:
        import aws_sdk_comprehendmedical.types.icd10_cm_attribute_list

        out["Attributes"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_attribute_list.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    if "traits" in value:
        import aws_sdk_comprehendmedical.types.icd10_cm_trait_list

        out["Traits"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_trait_list.serialize_aws_json_1_1(
                value["traits"]
            )
        )
    if "icd10_cm_concepts" in value:
        import aws_sdk_comprehendmedical.types.icd10_cm_concept_list

        out["ICD10CMConcepts"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_concept_list.serialize_aws_json_1_1(
                value["icd10_cm_concepts"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ICD10CMEntity:
    out: ICD10CMEntity = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Text" in data:
        out["text"] = data["Text"]
    if "Category" in data:
        import aws_sdk_comprehendmedical.types.icd10_cm_entity_category

        out["category"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_entity_category.deserialize_aws_json_1_1(
                data["Category"]
            )
        )
    if "Type" in data:
        import aws_sdk_comprehendmedical.types.icd10_cm_entity_type

        out["type"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_entity_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Score" in data:
        out["score"] = data["Score"]
    if "BeginOffset" in data:
        out["begin_offset"] = data["BeginOffset"]
    if "EndOffset" in data:
        out["end_offset"] = data["EndOffset"]
    if "Attributes" in data:
        import aws_sdk_comprehendmedical.types.icd10_cm_attribute_list

        out["attributes"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_attribute_list.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    if "Traits" in data:
        import aws_sdk_comprehendmedical.types.icd10_cm_trait_list

        out["traits"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_trait_list.deserialize_aws_json_1_1(
                data["Traits"]
            )
        )
    if "ICD10CMConcepts" in data:
        import aws_sdk_comprehendmedical.types.icd10_cm_concept_list

        out["icd10_cm_concepts"] = (
            aws_sdk_comprehendmedical.types.icd10_cm_concept_list.deserialize_aws_json_1_1(
                data["ICD10CMConcepts"]
            )
        )
    return out
