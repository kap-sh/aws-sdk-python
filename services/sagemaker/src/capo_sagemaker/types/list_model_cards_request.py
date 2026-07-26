"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListModelCardsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.model_card_sort_by
    import capo_sagemaker.types.model_card_sort_order
    import capo_sagemaker.types.model_card_status
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.timestamp


class ListModelCardsRequest(TypedDict, closed=True):
    creation_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Only list model cards that were created after the time specified.</p>"""
    creation_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Only list model cards that were created before the time specified.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of model cards to list.</p>"""
    name_contains: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>Only list model cards with names that contain the specified string.</p>"""
    model_card_status: NotRequired[
        "capo_sagemaker.types.model_card_status.ModelCardStatus"
    ]
    """<p>Only list model cards with the specified approval status.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response to a previous <code>ListModelCards</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of model cards, use the token in the next request.</p>"""
    sort_by: NotRequired["capo_sagemaker.types.model_card_sort_by.ModelCardSortBy"]
    """<p>Sort model cards by either name or creation time. Sorts by creation time by default.</p>"""
    sort_order: NotRequired[
        "capo_sagemaker.types.model_card_sort_order.ModelCardSortOrder"
    ]
    """<p>Sort model cards by ascending or descending order.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListModelCardsRequest) -> dict:
    out: dict = {}
    if "creation_time_after" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTimeAfter"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTimeBefore"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "model_card_status" in value:
        import capo_sagemaker.types.model_card_status

        out["ModelCardStatus"] = (
            capo_sagemaker.types.model_card_status.serialize_aws_json_1_1(
                value["model_card_status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort_by" in value:
        import capo_sagemaker.types.model_card_sort_by

        out["SortBy"] = capo_sagemaker.types.model_card_sort_by.serialize_aws_json_1_1(
            value["sort_by"]
        )
    if "sort_order" in value:
        import capo_sagemaker.types.model_card_sort_order

        out["SortOrder"] = (
            capo_sagemaker.types.model_card_sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListModelCardsRequest:
    out: ListModelCardsRequest = {}  # type: ignore[typeddict-item]
    if "CreationTimeAfter" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time_after"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "CreationTimeBefore" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time_before"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "ModelCardStatus" in data:
        import capo_sagemaker.types.model_card_status

        out["model_card_status"] = (
            capo_sagemaker.types.model_card_status.deserialize_aws_json_1_1(
                data["ModelCardStatus"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "SortBy" in data:
        import capo_sagemaker.types.model_card_sort_by

        out["sort_by"] = (
            capo_sagemaker.types.model_card_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import capo_sagemaker.types.model_card_sort_order

        out["sort_order"] = (
            capo_sagemaker.types.model_card_sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    return out
