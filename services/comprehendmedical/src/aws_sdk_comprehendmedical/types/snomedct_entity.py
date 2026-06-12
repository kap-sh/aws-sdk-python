"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTEntity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.float
    import aws_sdk_comprehendmedical.types.integer
    import aws_sdk_comprehendmedical.types.ontology_linking_bounded_length_string
    import aws_sdk_comprehendmedical.types.snomedct_attribute_list
    import aws_sdk_comprehendmedical.types.snomedct_concept_list
    import aws_sdk_comprehendmedical.types.snomedct_entity_category
    import aws_sdk_comprehendmedical.types.snomedct_entity_type
    import aws_sdk_comprehendmedical.types.snomedct_trait_list


class SNOMEDCTEntity(TypedDict):
    id: NotRequired["aws_sdk_comprehendmedical.types.integer.Integer"]
    """<p> The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier. </p>"""
    text: NotRequired[
        "aws_sdk_comprehendmedical.types.ontology_linking_bounded_length_string.OntologyLinkingBoundedLengthString"
    ]
    """<p> The segment of input text extracted as this entity. </p>"""
    category: NotRequired[
        "aws_sdk_comprehendmedical.types.snomedct_entity_category.SNOMEDCTEntityCategory"
    ]
    """<p> The category of the detected entity. Possible categories are MEDICAL_CONDITION, ANATOMY, or TEST_TREATMENT_PROCEDURE. </p>"""
    type: NotRequired[
        "aws_sdk_comprehendmedical.types.snomedct_entity_type.SNOMEDCTEntityType"
    ]
    """<p> Describes the specific type of entity with category of entities. Possible types include DX_NAME, ACUITY, DIRECTION, SYSTEM_ORGAN_SITE, TEST_NAME, TEST_VALUE, TEST_UNIT, PROCEDURE_NAME, or TREATMENT_NAME. </p>"""
    score: NotRequired["aws_sdk_comprehendmedical.types.float.Float"]
    """<p> The level of confidence that Amazon Comprehend Medical has in the accuracy of the detected entity. </p>"""
    begin_offset: NotRequired["aws_sdk_comprehendmedical.types.integer.Integer"]
    """<p> The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string. </p>"""
    end_offset: NotRequired["aws_sdk_comprehendmedical.types.integer.Integer"]
    """<p> The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string. </p>"""
    attributes: NotRequired[
        "aws_sdk_comprehendmedical.types.snomedct_attribute_list.SNOMEDCTAttributeList"
    ]
    """<p> An extracted segment of the text that is an attribute of an entity, or otherwise related to an entity, such as the dosage of a medication taken. </p>"""
    traits: NotRequired[
        "aws_sdk_comprehendmedical.types.snomedct_trait_list.SNOMEDCTTraitList"
    ]
    """<p> Contextual information for the entity. </p>"""
    snomedct_concepts: NotRequired[
        "aws_sdk_comprehendmedical.types.snomedct_concept_list.SNOMEDCTConceptList"
    ]
    """<p> The SNOMED concepts that the entity could refer to, along with a score indicating the likelihood of the match. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SNOMEDCTEntity) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "text" in value:
        out["Text"] = value["text"]
    if "category" in value:
        import aws_sdk_comprehendmedical.types.snomedct_entity_category

        out["Category"] = (
            aws_sdk_comprehendmedical.types.snomedct_entity_category.serialize_aws_json_1_1(
                value["category"]
            )
        )
    if "type" in value:
        import aws_sdk_comprehendmedical.types.snomedct_entity_type

        out["Type"] = (
            aws_sdk_comprehendmedical.types.snomedct_entity_type.serialize_aws_json_1_1(
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
        import aws_sdk_comprehendmedical.types.snomedct_attribute_list

        out["Attributes"] = (
            aws_sdk_comprehendmedical.types.snomedct_attribute_list.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    if "traits" in value:
        import aws_sdk_comprehendmedical.types.snomedct_trait_list

        out["Traits"] = (
            aws_sdk_comprehendmedical.types.snomedct_trait_list.serialize_aws_json_1_1(
                value["traits"]
            )
        )
    if "snomedct_concepts" in value:
        import aws_sdk_comprehendmedical.types.snomedct_concept_list

        out["SNOMEDCTConcepts"] = (
            aws_sdk_comprehendmedical.types.snomedct_concept_list.serialize_aws_json_1_1(
                value["snomedct_concepts"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SNOMEDCTEntity:
    out: SNOMEDCTEntity = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Text" in data:
        out["text"] = data["Text"]
    if "Category" in data:
        import aws_sdk_comprehendmedical.types.snomedct_entity_category

        out["category"] = (
            aws_sdk_comprehendmedical.types.snomedct_entity_category.deserialize_aws_json_1_1(
                data["Category"]
            )
        )
    if "Type" in data:
        import aws_sdk_comprehendmedical.types.snomedct_entity_type

        out["type"] = (
            aws_sdk_comprehendmedical.types.snomedct_entity_type.deserialize_aws_json_1_1(
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
        import aws_sdk_comprehendmedical.types.snomedct_attribute_list

        out["attributes"] = (
            aws_sdk_comprehendmedical.types.snomedct_attribute_list.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    if "Traits" in data:
        import aws_sdk_comprehendmedical.types.snomedct_trait_list

        out["traits"] = (
            aws_sdk_comprehendmedical.types.snomedct_trait_list.deserialize_aws_json_1_1(
                data["Traits"]
            )
        )
    if "SNOMEDCTConcepts" in data:
        import aws_sdk_comprehendmedical.types.snomedct_concept_list

        out["snomedct_concepts"] = (
            aws_sdk_comprehendmedical.types.snomedct_concept_list.deserialize_aws_json_1_1(
                data["SNOMEDCTConcepts"]
            )
        )
    return out
