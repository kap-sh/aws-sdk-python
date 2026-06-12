"""Generated from Smithy shape ``com.amazonaws.medialive#ListCloudWatchAlarmTemplateGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_cloud_watch_alarm_template_group_summary
    import aws_sdk_medialive.types.__string_min1_max2048


class ListCloudWatchAlarmTemplateGroupsResponse(TypedDict):
    cloud_watch_alarm_template_groups: NotRequired[
        "aws_sdk_medialive.types.__list_of_cloud_watch_alarm_template_group_summary.__listOfCloudWatchAlarmTemplateGroupSummary"
    ]
    next_token: NotRequired[
        "aws_sdk_medialive.types.__string_min1_max2048.__stringMin1Max2048"
    ]
    """A token used to retrieve the next set of results in paginated list responses."""


# --- restJson1 ser/de ---
def serialize_json(value: ListCloudWatchAlarmTemplateGroupsResponse) -> dict:
    out: dict = {}
    if "cloud_watch_alarm_template_groups" in value:
        import aws_sdk_medialive.types.__list_of_cloud_watch_alarm_template_group_summary

        out["cloudWatchAlarmTemplateGroups"] = (
            aws_sdk_medialive.types.__list_of_cloud_watch_alarm_template_group_summary.serialize_json(
                value["cloud_watch_alarm_template_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCloudWatchAlarmTemplateGroupsResponse:
    out: ListCloudWatchAlarmTemplateGroupsResponse = {}  # type: ignore[typeddict-item]
    if "cloudWatchAlarmTemplateGroups" in data:
        import aws_sdk_medialive.types.__list_of_cloud_watch_alarm_template_group_summary

        out["cloud_watch_alarm_template_groups"] = (
            aws_sdk_medialive.types.__list_of_cloud_watch_alarm_template_group_summary.deserialize_json(
                data["cloudWatchAlarmTemplateGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
