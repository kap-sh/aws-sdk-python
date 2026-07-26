"""Generated from Smithy shape ``com.amazonaws.wafv2#RateBasedStatementCustomKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.rate_based_statement_custom_key

RateBasedStatementCustomKeys: TypeAlias = list[
    "capo_wafv2.types.rate_based_statement_custom_key.RateBasedStatementCustomKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RateBasedStatementCustomKeys) -> list:
    import capo_wafv2.types.rate_based_statement_custom_key

    out: list = []
    for item in value:
        out.append(
            capo_wafv2.types.rate_based_statement_custom_key.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RateBasedStatementCustomKeys:
    import capo_wafv2.types.rate_based_statement_custom_key

    out: RateBasedStatementCustomKeys = []
    for item in data:
        out.append(
            capo_wafv2.types.rate_based_statement_custom_key.deserialize_aws_json_1_1(
                item
            )
        )
    return out
