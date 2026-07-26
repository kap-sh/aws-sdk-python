"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.float
    import capo_comprehendmedical.types.integer
    import capo_comprehendmedical.types.ontology_linking_bounded_length_string
    import capo_comprehendmedical.types.rx_norm_attribute_list
    import capo_comprehendmedical.types.rx_norm_concept_list
    import capo_comprehendmedical.types.rx_norm_entity_category
    import capo_comprehendmedical.types.rx_norm_entity_type
    import capo_comprehendmedical.types.rx_norm_trait_list


class RxNormEntity(TypedDict, closed=True):
    id: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p>The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier.</p>"""
    text: NotRequired[
        "capo_comprehendmedical.types.ontology_linking_bounded_length_string.OntologyLinkingBoundedLengthString"
    ]
    """<p>The segment of input text extracted from which the entity was detected.</p>"""
    category: NotRequired[
        "capo_comprehendmedical.types.rx_norm_entity_category.RxNormEntityCategory"
    ]
    """<p>The category of the entity. The recognized categories are <code>GENERIC</code> or <code>BRAND_NAME</code>.</p>"""
    type: NotRequired[
        "capo_comprehendmedical.types.rx_norm_entity_type.RxNormEntityType"
    ]
    """<p> Describes the specific type of entity. For InferRxNorm, the recognized entity type is <code>MEDICATION</code>.</p>"""
    score: NotRequired["capo_comprehendmedical.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend Medical has in the accuracy of the detected entity.</p>"""
    begin_offset: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p>The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string.</p>"""
    end_offset: NotRequired["capo_comprehendmedical.types.integer.Integer"]
    """<p>The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string.</p>"""
    attributes: NotRequired[
        "capo_comprehendmedical.types.rx_norm_attribute_list.RxNormAttributeList"
    ]
    """<p>The extracted attributes that relate to the entity. The attributes recognized by InferRxNorm are <code>DOSAGE</code>, <code>DURATION</code>, <code>FORM</code>, <code>FREQUENCY</code>, <code>RATE</code>, <code>ROUTE_OR_MODE</code>, and <code>STRENGTH</code>.</p>"""
    traits: NotRequired[
        "capo_comprehendmedical.types.rx_norm_trait_list.RxNormTraitList"
    ]
    """<p>Contextual information for the entity.</p>"""
    rx_norm_concepts: NotRequired[
        "capo_comprehendmedical.types.rx_norm_concept_list.RxNormConceptList"
    ]
    """<p>The RxNorm concepts that the entity could refer to, along with a score indicating the likelihood of the match.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RxNormEntity) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "text" in value:
        out["Text"] = value["text"]
    if "category" in value:
        import capo_comprehendmedical.types.rx_norm_entity_category

        out["Category"] = (
            capo_comprehendmedical.types.rx_norm_entity_category.serialize_aws_json_1_1(
                value["category"]
            )
        )
    if "type" in value:
        import capo_comprehendmedical.types.rx_norm_entity_type

        out["Type"] = (
            capo_comprehendmedical.types.rx_norm_entity_type.serialize_aws_json_1_1(
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
        import capo_comprehendmedical.types.rx_norm_attribute_list

        out["Attributes"] = (
            capo_comprehendmedical.types.rx_norm_attribute_list.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    if "traits" in value:
        import capo_comprehendmedical.types.rx_norm_trait_list

        out["Traits"] = (
            capo_comprehendmedical.types.rx_norm_trait_list.serialize_aws_json_1_1(
                value["traits"]
            )
        )
    if "rx_norm_concepts" in value:
        import capo_comprehendmedical.types.rx_norm_concept_list

        out["RxNormConcepts"] = (
            capo_comprehendmedical.types.rx_norm_concept_list.serialize_aws_json_1_1(
                value["rx_norm_concepts"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RxNormEntity:
    out: RxNormEntity = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Text" in data:
        out["text"] = data["Text"]
    if "Category" in data:
        import capo_comprehendmedical.types.rx_norm_entity_category

        out["category"] = (
            capo_comprehendmedical.types.rx_norm_entity_category.deserialize_aws_json_1_1(
                data["Category"]
            )
        )
    if "Type" in data:
        import capo_comprehendmedical.types.rx_norm_entity_type

        out["type"] = (
            capo_comprehendmedical.types.rx_norm_entity_type.deserialize_aws_json_1_1(
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
        import capo_comprehendmedical.types.rx_norm_attribute_list

        out["attributes"] = (
            capo_comprehendmedical.types.rx_norm_attribute_list.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    if "Traits" in data:
        import capo_comprehendmedical.types.rx_norm_trait_list

        out["traits"] = (
            capo_comprehendmedical.types.rx_norm_trait_list.deserialize_aws_json_1_1(
                data["Traits"]
            )
        )
    if "RxNormConcepts" in data:
        import capo_comprehendmedical.types.rx_norm_concept_list

        out["rx_norm_concepts"] = (
            capo_comprehendmedical.types.rx_norm_concept_list.deserialize_aws_json_1_1(
                data["RxNormConcepts"]
            )
        )
    return out
