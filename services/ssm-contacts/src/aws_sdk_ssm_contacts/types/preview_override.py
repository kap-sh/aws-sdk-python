"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#PreviewOverride``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.date_time
    import aws_sdk_ssm_contacts.types.rotation_override_preview_member_list


class PreviewOverride(TypedDict):
    new_members: NotRequired[
        "aws_sdk_ssm_contacts.types.rotation_override_preview_member_list.RotationOverridePreviewMemberList"
    ]
    """<p>Information about contacts to add to an on-call rotation override.</p>"""
    start_time: NotRequired["aws_sdk_ssm_contacts.types.date_time.DateTime"]
    """<p>Information about the time a rotation override would begin.</p>"""
    end_time: NotRequired["aws_sdk_ssm_contacts.types.date_time.DateTime"]
    """<p>Information about the time a rotation override would end.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreviewOverride) -> dict:
    out: dict = {}
    if "new_members" in value:
        import aws_sdk_ssm_contacts.types.rotation_override_preview_member_list

        out["NewMembers"] = (
            aws_sdk_ssm_contacts.types.rotation_override_preview_member_list.serialize_aws_json_1_1(
                value["new_members"]
            )
        )
    if "start_time" in value:
        import aws_sdk_ssm_contacts.types.date_time

        out["StartTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_ssm_contacts.types.date_time

        out["EndTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PreviewOverride:
    out: PreviewOverride = {}  # type: ignore[typeddict-item]
    if "NewMembers" in data:
        import aws_sdk_ssm_contacts.types.rotation_override_preview_member_list

        out["new_members"] = (
            aws_sdk_ssm_contacts.types.rotation_override_preview_member_list.deserialize_aws_json_1_1(
                data["NewMembers"]
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
    return out
