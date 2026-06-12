"""Generated from Smithy shape ``com.amazonaws.comprehend#ListDatasetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.dataset_properties_list
    import aws_sdk_comprehend.types.string


class ListDatasetsResponse(TypedDict):
    dataset_properties_list: NotRequired[
        "aws_sdk_comprehend.types.dataset_properties_list.DatasetPropertiesList"
    ]
    """<p>The dataset properties list.</p>"""
    next_token: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetsResponse) -> dict:
    out: dict = {}
    if "dataset_properties_list" in value:
        import aws_sdk_comprehend.types.dataset_properties_list

        out["DatasetPropertiesList"] = (
            aws_sdk_comprehend.types.dataset_properties_list.serialize_aws_json_1_1(
                value["dataset_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetsResponse:
    out: ListDatasetsResponse = {}  # type: ignore[typeddict-item]
    if "DatasetPropertiesList" in data:
        import aws_sdk_comprehend.types.dataset_properties_list

        out["dataset_properties_list"] = (
            aws_sdk_comprehend.types.dataset_properties_list.deserialize_aws_json_1_1(
                data["DatasetPropertiesList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
