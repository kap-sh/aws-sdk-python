"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListPreviewRotationShiftsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.date_time
    import aws_sdk_ssm_contacts.types.max_results
    import aws_sdk_ssm_contacts.types.override_list
    import aws_sdk_ssm_contacts.types.pagination_token
    import aws_sdk_ssm_contacts.types.recurrence_settings
    import aws_sdk_ssm_contacts.types.rotation_preview_member_list
    import aws_sdk_ssm_contacts.types.time_zone_id


class ListPreviewRotationShiftsRequest(TypedDict):
    rotation_start_time: NotRequired["aws_sdk_ssm_contacts.types.date_time.DateTime"]
    """<p>The date and time a rotation would begin. The first shift is calculated from this date and time.</p>"""
    start_time: NotRequired["aws_sdk_ssm_contacts.types.date_time.DateTime"]
    """<p>Used to filter the range of calculated shifts before sending the response back to the user. </p>"""
    end_time: "aws_sdk_ssm_contacts.types.date_time.DateTime"
    """<p>The date and time a rotation shift would end.</p>"""
    members: "aws_sdk_ssm_contacts.types.rotation_preview_member_list.RotationPreviewMemberList"
    """<p>The contacts that would be assigned to a rotation.</p>"""
    time_zone_id: "aws_sdk_ssm_contacts.types.time_zone_id.TimeZoneId"
    r"""<p>The time zone the rotation’s activity would be based on, in Internet Assigned Numbers Authority (IANA) format. For example: \"America/Los_Angeles\", \"UTC\", or \"Asia/Seoul\". </p>"""
    recurrence: "aws_sdk_ssm_contacts.types.recurrence_settings.RecurrenceSettings"
    """<p>Information about how long a rotation would last before restarting at the beginning of the shift order.</p>"""
    overrides: NotRequired["aws_sdk_ssm_contacts.types.override_list.OverrideList"]
    """<p>Information about changes that would be made in a rotation override.</p>"""
    next_token: NotRequired[
        "aws_sdk_ssm_contacts.types.pagination_token.PaginationToken"
    ]
    """<p>A token to start the list. This token is used to get the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_ssm_contacts.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that can be specified in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPreviewRotationShiftsRequest) -> dict:
    out: dict = {}
    if "rotation_start_time" in value:
        import aws_sdk_ssm_contacts.types.date_time

        out["RotationStartTime"] = (
            aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
                value["rotation_start_time"]
            )
        )
    if "start_time" in value:
        import aws_sdk_ssm_contacts.types.date_time

        out["StartTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    import aws_sdk_ssm_contacts.types.date_time

    out["EndTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
        value["end_time"]
    )
    import aws_sdk_ssm_contacts.types.rotation_preview_member_list

    out["Members"] = (
        aws_sdk_ssm_contacts.types.rotation_preview_member_list.serialize_aws_json_1_1(
            value["members"]
        )
    )
    out["TimeZoneId"] = value["time_zone_id"]
    import aws_sdk_ssm_contacts.types.recurrence_settings

    out["Recurrence"] = (
        aws_sdk_ssm_contacts.types.recurrence_settings.serialize_aws_json_1_1(
            value["recurrence"]
        )
    )
    if "overrides" in value:
        import aws_sdk_ssm_contacts.types.override_list

        out["Overrides"] = (
            aws_sdk_ssm_contacts.types.override_list.serialize_aws_json_1_1(
                value["overrides"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPreviewRotationShiftsRequest:
    out: ListPreviewRotationShiftsRequest = {}  # type: ignore[typeddict-item]
    if "RotationStartTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["rotation_start_time"] = (
            aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["RotationStartTime"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["start_time"] = (
            aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["end_time"] = aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    else:
        raise DeserializationError("ListPreviewRotationShiftsRequest.end_time required")
    if "Members" in data:
        import aws_sdk_ssm_contacts.types.rotation_preview_member_list

        out["members"] = (
            aws_sdk_ssm_contacts.types.rotation_preview_member_list.deserialize_aws_json_1_1(
                data["Members"]
            )
        )
    else:
        raise DeserializationError("ListPreviewRotationShiftsRequest.members required")
    if "TimeZoneId" in data:
        out["time_zone_id"] = data["TimeZoneId"]
    else:
        raise DeserializationError(
            "ListPreviewRotationShiftsRequest.time_zone_id required"
        )
    if "Recurrence" in data:
        import aws_sdk_ssm_contacts.types.recurrence_settings

        out["recurrence"] = (
            aws_sdk_ssm_contacts.types.recurrence_settings.deserialize_aws_json_1_1(
                data["Recurrence"]
            )
        )
    else:
        raise DeserializationError(
            "ListPreviewRotationShiftsRequest.recurrence required"
        )
    if "Overrides" in data:
        import aws_sdk_ssm_contacts.types.override_list

        out["overrides"] = (
            aws_sdk_ssm_contacts.types.override_list.deserialize_aws_json_1_1(
                data["Overrides"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
