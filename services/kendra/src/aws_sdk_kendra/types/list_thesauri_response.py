"""Generated from Smithy shape ``com.amazonaws.kendra#ListThesauriResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.next_token
    import aws_sdk_kendra.types.thesaurus_summary_items


class ListThesauriResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_kendra.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Kendra returns this token that you can use in the subsequent request to retrieve the next set of thesauri. </p>"""
    thesaurus_summary_items: NotRequired[
        "aws_sdk_kendra.types.thesaurus_summary_items.ThesaurusSummaryItems"
    ]
    """<p>An array of summary information for a thesaurus or multiple thesauri.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListThesauriResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "thesaurus_summary_items" in value:
        import aws_sdk_kendra.types.thesaurus_summary_items

        out["ThesaurusSummaryItems"] = (
            aws_sdk_kendra.types.thesaurus_summary_items.serialize_aws_json_1_1(
                value["thesaurus_summary_items"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListThesauriResponse:
    out: ListThesauriResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ThesaurusSummaryItems" in data:
        import aws_sdk_kendra.types.thesaurus_summary_items

        out["thesaurus_summary_items"] = (
            aws_sdk_kendra.types.thesaurus_summary_items.deserialize_aws_json_1_1(
                data["ThesaurusSummaryItems"]
            )
        )
    return out
