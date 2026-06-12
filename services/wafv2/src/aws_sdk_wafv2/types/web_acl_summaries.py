"""Generated from Smithy shape ``com.amazonaws.wafv2#WebACLSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.web_acl_summary

WebACLSummaries: TypeAlias = list["aws_sdk_wafv2.types.web_acl_summary.WebACLSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebACLSummaries) -> list:
    import aws_sdk_wafv2.types.web_acl_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_wafv2.types.web_acl_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> WebACLSummaries:
    import aws_sdk_wafv2.types.web_acl_summary

    out: WebACLSummaries = []
    for item in data:
        out.append(aws_sdk_wafv2.types.web_acl_summary.deserialize_aws_json_1_1(item))
    return out
