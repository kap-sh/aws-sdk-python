"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeUpdateDirectoryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.next_token
    import aws_sdk_directory_service.types.update_activities


class DescribeUpdateDirectoryResult(TypedDict, closed=True):
    update_activities: NotRequired[
        "aws_sdk_directory_service.types.update_activities.UpdateActivities"
    ]
    """<p> The list of update activities on a directory for the requested update type. </p>"""
    next_token: NotRequired["aws_sdk_directory_service.types.next_token.NextToken"]
    """<p> If not null, more results are available. Pass this value for the <code>NextToken</code> parameter. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUpdateDirectoryResult) -> dict:
    out: dict = {}
    if "update_activities" in value:
        import aws_sdk_directory_service.types.update_activities

        out["UpdateActivities"] = (
            aws_sdk_directory_service.types.update_activities.serialize_aws_json_1_1(
                value["update_activities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUpdateDirectoryResult:
    out: DescribeUpdateDirectoryResult = {}  # type: ignore[typeddict-item]
    if "UpdateActivities" in data:
        import aws_sdk_directory_service.types.update_activities

        out["update_activities"] = (
            aws_sdk_directory_service.types.update_activities.deserialize_aws_json_1_1(
                data["UpdateActivities"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
