"""Generated from Smithy shape ``com.amazonaws.wafregional#SqlInjectionMatchSetUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.sql_injection_match_set_update

SqlInjectionMatchSetUpdates: TypeAlias = list[
    "aws_sdk_waf_regional.types.sql_injection_match_set_update.SqlInjectionMatchSetUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlInjectionMatchSetUpdates) -> list:
    import aws_sdk_waf_regional.types.sql_injection_match_set_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_waf_regional.types.sql_injection_match_set_update.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SqlInjectionMatchSetUpdates:
    import aws_sdk_waf_regional.types.sql_injection_match_set_update

    out: SqlInjectionMatchSetUpdates = []
    for item in data:
        out.append(
            aws_sdk_waf_regional.types.sql_injection_match_set_update.deserialize_aws_json_1_1(
                item
            )
        )
    return out
