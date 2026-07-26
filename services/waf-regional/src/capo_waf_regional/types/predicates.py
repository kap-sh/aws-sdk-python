"""Generated from Smithy shape ``com.amazonaws.wafregional#Predicates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf_regional.types.predicate

Predicates: TypeAlias = list["capo_waf_regional.types.predicate.Predicate"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Predicates) -> list:
    import capo_waf_regional.types.predicate

    out: list = []
    for item in value:
        out.append(capo_waf_regional.types.predicate.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Predicates:
    import capo_waf_regional.types.predicate

    out: Predicates = []
    for item in data:
        out.append(capo_waf_regional.types.predicate.deserialize_aws_json_1_1(item))
    return out
