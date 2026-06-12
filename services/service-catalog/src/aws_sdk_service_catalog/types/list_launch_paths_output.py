"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListLaunchPathsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.launch_path_summaries
    import aws_sdk_service_catalog.types.page_token


class ListLaunchPathsOutput(TypedDict):
    launch_path_summaries: NotRequired[
        "aws_sdk_service_catalog.types.launch_path_summaries.LaunchPathSummaries"
    ]
    """<p>Information about the launch path.</p>"""
    next_page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLaunchPathsOutput) -> dict:
    out: dict = {}
    if "launch_path_summaries" in value:
        import aws_sdk_service_catalog.types.launch_path_summaries

        out["LaunchPathSummaries"] = (
            aws_sdk_service_catalog.types.launch_path_summaries.serialize_aws_json_1_1(
                value["launch_path_summaries"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLaunchPathsOutput:
    out: ListLaunchPathsOutput = {}  # type: ignore[typeddict-item]
    if "LaunchPathSummaries" in data:
        import aws_sdk_service_catalog.types.launch_path_summaries

        out["launch_path_summaries"] = (
            aws_sdk_service_catalog.types.launch_path_summaries.deserialize_aws_json_1_1(
                data["LaunchPathSummaries"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
