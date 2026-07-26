"""Generated from Smithy shape ``com.amazonaws.waf#SqlInjectionMatchSetUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf.types.sql_injection_match_set_update

SqlInjectionMatchSetUpdates: TypeAlias = list[
    "capo_waf.types.sql_injection_match_set_update.SqlInjectionMatchSetUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlInjectionMatchSetUpdates) -> list:
    import capo_waf.types.sql_injection_match_set_update

    out: list = []
    for item in value:
        out.append(
            capo_waf.types.sql_injection_match_set_update.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SqlInjectionMatchSetUpdates:
    import capo_waf.types.sql_injection_match_set_update

    out: SqlInjectionMatchSetUpdates = []
    for item in data:
        out.append(
            capo_waf.types.sql_injection_match_set_update.deserialize_aws_json_1_1(item)
        )
    return out
