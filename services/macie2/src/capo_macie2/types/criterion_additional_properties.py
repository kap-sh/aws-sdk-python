"""Generated from Smithy shape ``com.amazonaws.macie2#CriterionAdditionalProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of__string
    import capo_macie2.types.__long


class CriterionAdditionalProperties(TypedDict, closed=True):
    eq: NotRequired["capo_macie2.types.__list_of__string.__listOf__string"]
    """<p>The value for the property matches (equals) the specified value. If you specify multiple values, Macie uses OR logic to join the values.</p>"""
    eq_exact_match: NotRequired["capo_macie2.types.__list_of__string.__listOf__string"]
    """<p>The value for the property exclusively matches (equals an exact match for) all the specified values. If you specify multiple values, Amazon Macie uses AND logic to join the values.</p> <p>You can use this operator with the following properties: customDataIdentifiers.detections.arn, customDataIdentifiers.detections.name, resourcesAffected.s3Bucket.tags.key, resourcesAffected.s3Bucket.tags.value, resourcesAffected.s3Object.tags.key, resourcesAffected.s3Object.tags.value, sensitiveData.category, and sensitiveData.detections.type.</p>"""
    gt: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The value for the property is greater than the specified value.</p>"""
    gte: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The value for the property is greater than or equal to the specified value.</p>"""
    lt: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The value for the property is less than the specified value.</p>"""
    lte: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The value for the property is less than or equal to the specified value.</p>"""
    neq: NotRequired["capo_macie2.types.__list_of__string.__listOf__string"]
    """<p>The value for the property doesn't match (doesn't equal) the specified value. If you specify multiple values, Macie uses OR logic to join the values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CriterionAdditionalProperties) -> dict:
    out: dict = {}
    if "eq" in value:
        import capo_macie2.types.__list_of__string

        out["eq"] = capo_macie2.types.__list_of__string.serialize_json(value["eq"])
    if "eq_exact_match" in value:
        import capo_macie2.types.__list_of__string

        out["eqExactMatch"] = capo_macie2.types.__list_of__string.serialize_json(
            value["eq_exact_match"]
        )
    if "gt" in value:
        out["gt"] = value["gt"]
    if "gte" in value:
        out["gte"] = value["gte"]
    if "lt" in value:
        out["lt"] = value["lt"]
    if "lte" in value:
        out["lte"] = value["lte"]
    if "neq" in value:
        import capo_macie2.types.__list_of__string

        out["neq"] = capo_macie2.types.__list_of__string.serialize_json(value["neq"])
    return out


def deserialize_json(data: dict) -> CriterionAdditionalProperties:
    out: CriterionAdditionalProperties = {}  # type: ignore[typeddict-item]
    if "eq" in data:
        import capo_macie2.types.__list_of__string

        out["eq"] = capo_macie2.types.__list_of__string.deserialize_json(data["eq"])
    if "eqExactMatch" in data:
        import capo_macie2.types.__list_of__string

        out["eq_exact_match"] = capo_macie2.types.__list_of__string.deserialize_json(
            data["eqExactMatch"]
        )
    if "gt" in data:
        out["gt"] = data["gt"]
    if "gte" in data:
        out["gte"] = data["gte"]
    if "lt" in data:
        out["lt"] = data["lt"]
    if "lte" in data:
        out["lte"] = data["lte"]
    if "neq" in data:
        import capo_macie2.types.__list_of__string

        out["neq"] = capo_macie2.types.__list_of__string.deserialize_json(data["neq"])
    return out
