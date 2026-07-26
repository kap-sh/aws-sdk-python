"""Generated from Smithy shape ``com.amazonaws.forecast#ListDatasetGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.dataset_groups
    import capo_forecast.types.next_token


class ListDatasetGroupsResponse(TypedDict, closed=True):
    dataset_groups: NotRequired["capo_forecast.types.dataset_groups.DatasetGroups"]
    """<p>An array of objects that summarize each dataset group's properties.</p>"""
    next_token: NotRequired["capo_forecast.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of results, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetGroupsResponse) -> dict:
    out: dict = {}
    if "dataset_groups" in value:
        import capo_forecast.types.dataset_groups

        out["DatasetGroups"] = (
            capo_forecast.types.dataset_groups.serialize_aws_json_1_1(
                value["dataset_groups"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetGroupsResponse:
    out: ListDatasetGroupsResponse = {}  # type: ignore[typeddict-item]
    if "DatasetGroups" in data:
        import capo_forecast.types.dataset_groups

        out["dataset_groups"] = (
            capo_forecast.types.dataset_groups.deserialize_aws_json_1_1(
                data["DatasetGroups"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
