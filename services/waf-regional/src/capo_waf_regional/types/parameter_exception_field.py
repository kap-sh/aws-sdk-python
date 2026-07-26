"""Generated from Smithy shape ``com.amazonaws.wafregional#ParameterExceptionField``."""

from typing import Literal, TypeAlias, cast

ParameterExceptionField: TypeAlias = Literal[
    "CHANGE_ACTION",
    "WAF_ACTION",
    "WAF_OVERRIDE_ACTION",
    "PREDICATE_TYPE",
    "IPSET_TYPE",
    "BYTE_MATCH_FIELD_TYPE",
    "SQL_INJECTION_MATCH_FIELD_TYPE",
    "BYTE_MATCH_TEXT_TRANSFORMATION",
    "BYTE_MATCH_POSITIONAL_CONSTRAINT",
    "SIZE_CONSTRAINT_COMPARISON_OPERATOR",
    "GEO_MATCH_LOCATION_TYPE",
    "GEO_MATCH_LOCATION_VALUE",
    "RATE_KEY",
    "RULE_TYPE",
    "NEXT_MARKER",
    "RESOURCE_ARN",
    "TAGS",
    "TAG_KEYS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterExceptionField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParameterExceptionField:
    return cast(ParameterExceptionField, data)
