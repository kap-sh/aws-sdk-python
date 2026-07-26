"""Generated from Smithy shape ``com.amazonaws.wafregional#XssMatchSetUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf_regional.types.xss_match_set_update

XssMatchSetUpdates: TypeAlias = list[
    "capo_waf_regional.types.xss_match_set_update.XssMatchSetUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XssMatchSetUpdates) -> list:
    import capo_waf_regional.types.xss_match_set_update

    out: list = []
    for item in value:
        out.append(
            capo_waf_regional.types.xss_match_set_update.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> XssMatchSetUpdates:
    import capo_waf_regional.types.xss_match_set_update

    out: XssMatchSetUpdates = []
    for item in data:
        out.append(
            capo_waf_regional.types.xss_match_set_update.deserialize_aws_json_1_1(item)
        )
    return out
