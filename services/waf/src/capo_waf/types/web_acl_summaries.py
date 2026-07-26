"""Generated from Smithy shape ``com.amazonaws.waf#WebACLSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf.types.web_acl_summary

WebACLSummaries: TypeAlias = list["capo_waf.types.web_acl_summary.WebACLSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebACLSummaries) -> list:
    import capo_waf.types.web_acl_summary

    out: list = []
    for item in value:
        out.append(capo_waf.types.web_acl_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> WebACLSummaries:
    import capo_waf.types.web_acl_summary

    out: WebACLSummaries = []
    for item in data:
        out.append(capo_waf.types.web_acl_summary.deserialize_aws_json_1_1(item))
    return out
