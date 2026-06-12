"""Generated from Smithy shape ``com.amazonaws.wafregional#SqlInjectionMatchTuples``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.sql_injection_match_tuple

SqlInjectionMatchTuples: TypeAlias = list[
    "aws_sdk_waf_regional.types.sql_injection_match_tuple.SqlInjectionMatchTuple"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlInjectionMatchTuples) -> list:
    import aws_sdk_waf_regional.types.sql_injection_match_tuple

    out: list = []
    for item in value:
        out.append(
            aws_sdk_waf_regional.types.sql_injection_match_tuple.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SqlInjectionMatchTuples:
    import aws_sdk_waf_regional.types.sql_injection_match_tuple

    out: SqlInjectionMatchTuples = []
    for item in data:
        out.append(
            aws_sdk_waf_regional.types.sql_injection_match_tuple.deserialize_aws_json_1_1(
                item
            )
        )
    return out
