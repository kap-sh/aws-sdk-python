"""Generated from Smithy shape ``com.amazonaws.macie2#BucketCriteriaAdditionalProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of__string
    import capo_macie2.types.__long
    import capo_macie2.types.__string


class BucketCriteriaAdditionalProperties(TypedDict, closed=True):
    eq: NotRequired["capo_macie2.types.__list_of__string.__listOf__string"]
    """<p>The value for the property matches (equals) the specified value. If you specify multiple values, Amazon Macie uses OR logic to join the values.</p>"""
    gt: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The value for the property is greater than the specified value.</p>"""
    gte: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The value for the property is greater than or equal to the specified value.</p>"""
    lt: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The value for the property is less than the specified value.</p>"""
    lte: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The value for the property is less than or equal to the specified value.</p>"""
    neq: NotRequired["capo_macie2.types.__list_of__string.__listOf__string"]
    """<p>The value for the property doesn't match (doesn't equal) the specified value. If you specify multiple values, Amazon Macie uses OR logic to join the values.</p>"""
    prefix: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The name of the bucket begins with the specified value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BucketCriteriaAdditionalProperties) -> dict:
    out: dict = {}
    if "eq" in value:
        import capo_macie2.types.__list_of__string

        out["eq"] = capo_macie2.types.__list_of__string.serialize_json(value["eq"])
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
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> BucketCriteriaAdditionalProperties:
    out: BucketCriteriaAdditionalProperties = {}  # type: ignore[typeddict-item]
    if "eq" in data:
        import capo_macie2.types.__list_of__string

        out["eq"] = capo_macie2.types.__list_of__string.deserialize_json(data["eq"])
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
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    return out
