"""Generated from Smithy shape ``com.amazonaws.waf#XssMatchTuples``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf.types.xss_match_tuple

XssMatchTuples: TypeAlias = list["capo_waf.types.xss_match_tuple.XssMatchTuple"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XssMatchTuples) -> list:
    import capo_waf.types.xss_match_tuple

    out: list = []
    for item in value:
        out.append(capo_waf.types.xss_match_tuple.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> XssMatchTuples:
    import capo_waf.types.xss_match_tuple

    out: XssMatchTuples = []
    for item in data:
        out.append(capo_waf.types.xss_match_tuple.deserialize_aws_json_1_1(item))
    return out
