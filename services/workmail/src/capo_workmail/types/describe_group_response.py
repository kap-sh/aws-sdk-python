"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.boolean
    import capo_workmail.types.email_address
    import capo_workmail.types.entity_state
    import capo_workmail.types.group_name
    import capo_workmail.types.timestamp
    import capo_workmail.types.work_mail_identifier


class DescribeGroupResponse(TypedDict, closed=True):
    group_id: NotRequired["capo_workmail.types.work_mail_identifier.WorkMailIdentifier"]
    """<p>The identifier of the described group.</p>"""
    name: NotRequired["capo_workmail.types.group_name.GroupName"]
    """<p>The name of the described group.</p>"""
    email: NotRequired["capo_workmail.types.email_address.EmailAddress"]
    """<p>The email of the described group.</p>"""
    state: NotRequired["capo_workmail.types.entity_state.EntityState"]
    """<p>The state of the user: enabled (registered to WorkMail) or disabled (deregistered or never registered to WorkMail).</p>"""
    enabled_date: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date and time when a user was registered to WorkMail, in UNIX epoch time format.</p>"""
    disabled_date: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date and time when a user was deregistered from WorkMail, in UNIX epoch time format.</p>"""
    hidden_from_global_address_list: "capo_workmail.types.boolean.Boolean"
    """<p>If the value is set to <i>true</i>, the group is hidden from the address book.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGroupResponse) -> dict:
    out: dict = {}
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "email" in value:
        out["Email"] = value["email"]
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
    out["HiddenFromGlobalAddressList"] = value.get(
        "hidden_from_global_address_list", False
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGroupResponse:
    out: DescribeGroupResponse = {}  # type: ignore[typeddict-item]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Email" in data:
        out["email"] = data["Email"]
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
    if "HiddenFromGlobalAddressList" in data:
        out["hidden_from_global_address_list"] = data["HiddenFromGlobalAddressList"]
    else:
        out["hidden_from_global_address_list"] = False
    return out
