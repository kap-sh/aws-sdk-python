"""Generated from Smithy shape ``com.amazonaws.wafv2#CreateWebACLResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.web_acl_summary


class CreateWebACLResponse(TypedDict):
    summary: NotRequired["aws_sdk_wafv2.types.web_acl_summary.WebACLSummary"]
    """<p>High-level information about a <a>WebACL</a>, returned by operations like create and list. This provides information like the ID, that you can use to retrieve and manage a <code>WebACL</code>, and the ARN, that you provide to operations like <a>AssociateWebACL</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWebACLResponse) -> dict:
    out: dict = {}
    if "summary" in value:
        import aws_sdk_wafv2.types.web_acl_summary

        out["Summary"] = aws_sdk_wafv2.types.web_acl_summary.serialize_aws_json_1_1(
            value["summary"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWebACLResponse:
    out: CreateWebACLResponse = {}  # type: ignore[typeddict-item]
    if "Summary" in data:
        import aws_sdk_wafv2.types.web_acl_summary

        out["summary"] = aws_sdk_wafv2.types.web_acl_summary.deserialize_aws_json_1_1(
            data["Summary"]
        )
    return out
