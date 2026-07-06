"""Generated from Smithy shape ``com.amazonaws.kendra#ListFaqsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.faq_summary_items
    import aws_sdk_kendra.types.next_token


class ListFaqsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_kendra.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Kendra returns this token that you can use in the subsequent request to retrieve the next set of FAQs.</p>"""
    faq_summary_items: NotRequired[
        "aws_sdk_kendra.types.faq_summary_items.FaqSummaryItems"
    ]
    """<p>Summary information about the FAQs for a specified index.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFaqsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "faq_summary_items" in value:
        import aws_sdk_kendra.types.faq_summary_items

        out["FaqSummaryItems"] = (
            aws_sdk_kendra.types.faq_summary_items.serialize_aws_json_1_1(
                value["faq_summary_items"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFaqsResponse:
    out: ListFaqsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "FaqSummaryItems" in data:
        import aws_sdk_kendra.types.faq_summary_items

        out["faq_summary_items"] = (
            aws_sdk_kendra.types.faq_summary_items.deserialize_aws_json_1_1(
                data["FaqSummaryItems"]
            )
        )
    return out
