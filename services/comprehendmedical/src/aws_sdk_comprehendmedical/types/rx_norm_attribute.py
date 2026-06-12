"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormAttribute``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.float
    import aws_sdk_comprehendmedical.types.integer
    import aws_sdk_comprehendmedical.types.rx_norm_attribute_type
    import aws_sdk_comprehendmedical.types.rx_norm_trait_list
    import aws_sdk_comprehendmedical.types.string


class RxNormAttribute(TypedDict):
    type: NotRequired[
        "aws_sdk_comprehendmedical.types.rx_norm_attribute_type.RxNormAttributeType"
    ]
    """<p>The type of attribute. The types of attributes recognized by InferRxNorm are <code>BRAND_NAME</code> and <code>GENERIC_NAME</code>.</p>"""
    score: NotRequired["aws_sdk_comprehendmedical.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as an attribute.</p>"""
    relationship_score: NotRequired["aws_sdk_comprehendmedical.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend Medical has that the attribute is accurately linked to an entity.</p>"""
    id: NotRequired["aws_sdk_comprehendmedical.types.integer.Integer"]
    """<p>The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier.</p>"""
    begin_offset: NotRequired["aws_sdk_comprehendmedical.types.integer.Integer"]
    """<p>The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string.</p>"""
    end_offset: NotRequired["aws_sdk_comprehendmedical.types.integer.Integer"]
    """<p>The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.</p>"""
    text: NotRequired["aws_sdk_comprehendmedical.types.string.String"]
    """<p>The segment of input text which corresponds to the detected attribute.</p>"""
    traits: NotRequired[
        "aws_sdk_comprehendmedical.types.rx_norm_trait_list.RxNormTraitList"
    ]
    """<p>Contextual information for the attribute. InferRxNorm recognizes the trait <code>NEGATION</code> for attributes, i.e. that the patient is not taking a specific dose or form of a medication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RxNormAttribute) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_comprehendmedical.types.rx_norm_attribute_type

        out["Type"] = (
            aws_sdk_comprehendmedical.types.rx_norm_attribute_type.serialize_aws_json_1_1(
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
        import aws_sdk_comprehendmedical.types.rx_norm_trait_list

        out["Traits"] = (
            aws_sdk_comprehendmedical.types.rx_norm_trait_list.serialize_aws_json_1_1(
                value["traits"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RxNormAttribute:
    out: RxNormAttribute = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_comprehendmedical.types.rx_norm_attribute_type

        out["type"] = (
            aws_sdk_comprehendmedical.types.rx_norm_attribute_type.deserialize_aws_json_1_1(
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
        import aws_sdk_comprehendmedical.types.rx_norm_trait_list

        out["traits"] = (
            aws_sdk_comprehendmedical.types.rx_norm_trait_list.deserialize_aws_json_1_1(
                data["Traits"]
            )
        )
    return out
