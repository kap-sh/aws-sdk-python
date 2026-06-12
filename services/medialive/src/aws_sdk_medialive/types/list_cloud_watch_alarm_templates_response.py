"""Generated from Smithy shape ``com.amazonaws.medialive#ListCloudWatchAlarmTemplatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_cloud_watch_alarm_template_summary
    import aws_sdk_medialive.types.__string_min1_max2048


class ListCloudWatchAlarmTemplatesResponse(TypedDict):
    cloud_watch_alarm_templates: NotRequired[
        "aws_sdk_medialive.types.__list_of_cloud_watch_alarm_template_summary.__listOfCloudWatchAlarmTemplateSummary"
    ]
    next_token: NotRequired[
        "aws_sdk_medialive.types.__string_min1_max2048.__stringMin1Max2048"
    ]
    """A token used to retrieve the next set of results in paginated list responses."""


# --- restJson1 ser/de ---
def serialize_json(value: ListCloudWatchAlarmTemplatesResponse) -> dict:
    out: dict = {}
    if "cloud_watch_alarm_templates" in value:
        import aws_sdk_medialive.types.__list_of_cloud_watch_alarm_template_summary

        out["cloudWatchAlarmTemplates"] = (
            aws_sdk_medialive.types.__list_of_cloud_watch_alarm_template_summary.serialize_json(
                value["cloud_watch_alarm_templates"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCloudWatchAlarmTemplatesResponse:
    out: ListCloudWatchAlarmTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "cloudWatchAlarmTemplates" in data:
        import aws_sdk_medialive.types.__list_of_cloud_watch_alarm_template_summary

        out["cloud_watch_alarm_templates"] = (
            aws_sdk_medialive.types.__list_of_cloud_watch_alarm_template_summary.deserialize_json(
                data["cloudWatchAlarmTemplates"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
