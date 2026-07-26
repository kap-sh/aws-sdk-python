"""Generated from Smithy shape ``com.amazonaws.glue#SearchPropertyPredicates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.property_predicate

SearchPropertyPredicates: TypeAlias = list[
    "capo_glue.types.property_predicate.PropertyPredicate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchPropertyPredicates) -> list:
    import capo_glue.types.property_predicate

    out: list = []
    for item in value:
        out.append(capo_glue.types.property_predicate.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SearchPropertyPredicates:
    import capo_glue.types.property_predicate

    out: SearchPropertyPredicates = []
    for item in data:
        out.append(capo_glue.types.property_predicate.deserialize_aws_json_1_1(item))
    return out
