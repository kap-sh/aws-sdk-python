"""Generated from Smithy shape ``com.amazonaws.kendra#ListIndicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.index_configuration_summary_list
    import capo_kendra.types.next_token


class ListIndicesResponse(TypedDict, closed=True):
    index_configuration_summary_items: NotRequired[
        "capo_kendra.types.index_configuration_summary_list.IndexConfigurationSummaryList"
    ]
    """<p>An array of summary information on the configuration of one or more indexes.</p>"""
    next_token: NotRequired["capo_kendra.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Kendra returns this token that you can use in the subsequent request to retrieve the next set of indexes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIndicesResponse) -> dict:
    out: dict = {}
    if "index_configuration_summary_items" in value:
        import capo_kendra.types.index_configuration_summary_list

        out["IndexConfigurationSummaryItems"] = (
            capo_kendra.types.index_configuration_summary_list.serialize_aws_json_1_1(
                value["index_configuration_summary_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIndicesResponse:
    out: ListIndicesResponse = {}  # type: ignore[typeddict-item]
    if "IndexConfigurationSummaryItems" in data:
        import capo_kendra.types.index_configuration_summary_list

        out["index_configuration_summary_items"] = (
            capo_kendra.types.index_configuration_summary_list.deserialize_aws_json_1_1(
                data["IndexConfigurationSummaryItems"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
