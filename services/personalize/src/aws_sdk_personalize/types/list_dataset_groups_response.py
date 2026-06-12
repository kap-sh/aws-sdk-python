"""Generated from Smithy shape ``com.amazonaws.personalize#ListDatasetGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.dataset_groups
    import aws_sdk_personalize.types.next_token


class ListDatasetGroupsResponse(TypedDict):
    dataset_groups: NotRequired[
        "aws_sdk_personalize.types.dataset_groups.DatasetGroups"
    ]
    """<p>The list of your dataset groups.</p>"""
    next_token: NotRequired["aws_sdk_personalize.types.next_token.NextToken"]
    """<p>A token for getting the next set of dataset groups (if they exist).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetGroupsResponse) -> dict:
    out: dict = {}
    if "dataset_groups" in value:
        import aws_sdk_personalize.types.dataset_groups

        out["datasetGroups"] = (
            aws_sdk_personalize.types.dataset_groups.serialize_aws_json_1_1(
                value["dataset_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetGroupsResponse:
    out: ListDatasetGroupsResponse = {}  # type: ignore[typeddict-item]
    if "datasetGroups" in data:
        import aws_sdk_personalize.types.dataset_groups

        out["dataset_groups"] = (
            aws_sdk_personalize.types.dataset_groups.deserialize_aws_json_1_1(
                data["datasetGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
