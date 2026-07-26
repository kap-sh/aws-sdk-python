"""Generated from Smithy shape ``com.amazonaws.wafv2#CreateIPSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.ip_set_summary


class CreateIPSetResponse(TypedDict, closed=True):
    summary: NotRequired["capo_wafv2.types.ip_set_summary.IPSetSummary"]
    """<p>High-level information about an <a>IPSet</a>, returned by operations like create and list. This provides information like the ID, that you can use to retrieve and manage an <code>IPSet</code>, and the ARN, that you provide to the <a>IPSetReferenceStatement</a> to use the address set in a <a>Rule</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateIPSetResponse) -> dict:
    out: dict = {}
    if "summary" in value:
        import capo_wafv2.types.ip_set_summary

        out["Summary"] = capo_wafv2.types.ip_set_summary.serialize_aws_json_1_1(
            value["summary"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateIPSetResponse:
    out: CreateIPSetResponse = {}  # type: ignore[typeddict-item]
    if "Summary" in data:
        import capo_wafv2.types.ip_set_summary

        out["summary"] = capo_wafv2.types.ip_set_summary.deserialize_aws_json_1_1(
            data["Summary"]
        )
    return out
