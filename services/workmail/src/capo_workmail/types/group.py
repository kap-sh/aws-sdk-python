"""Generated from Smithy shape ``com.amazonaws.workmail#Group``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.email_address
    import capo_workmail.types.entity_state
    import capo_workmail.types.group_name
    import capo_workmail.types.timestamp
    import capo_workmail.types.work_mail_identifier


class Group(TypedDict, closed=True):
    id: NotRequired["capo_workmail.types.work_mail_identifier.WorkMailIdentifier"]
    """<p>The identifier of the group.</p>"""
    email: NotRequired["capo_workmail.types.email_address.EmailAddress"]
    """<p>The email of the group.</p>"""
    name: NotRequired["capo_workmail.types.group_name.GroupName"]
    """<p>The name of the group.</p>"""
    state: NotRequired["capo_workmail.types.entity_state.EntityState"]
    """<p>The state of the group, which can be ENABLED, DISABLED, or DELETED.</p>"""
    enabled_date: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date indicating when the group was enabled for WorkMail use.</p>"""
    disabled_date: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date indicating when the group was disabled from WorkMail use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Group) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "email" in value:
        out["Email"] = value["email"]
    if "name" in value:
        out["Name"] = value["name"]
    if "state" in value:
        import capo_workmail.types.entity_state

        out["State"] = capo_workmail.types.entity_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "enabled_date" in value:
        import capo_workmail.types.timestamp

        out["EnabledDate"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["enabled_date"]
        )
    if "disabled_date" in value:
        import capo_workmail.types.timestamp

        out["DisabledDate"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["disabled_date"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Group:
    out: Group = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Email" in data:
        out["email"] = data["Email"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "State" in data:
        import capo_workmail.types.entity_state

        out["state"] = capo_workmail.types.entity_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "EnabledDate" in data:
        import capo_workmail.types.timestamp

        out["enabled_date"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["EnabledDate"]
        )
    if "DisabledDate" in data:
        import capo_workmail.types.timestamp

        out["disabled_date"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["DisabledDate"]
        )
    return out
