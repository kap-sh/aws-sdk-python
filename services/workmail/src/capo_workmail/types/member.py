"""Generated from Smithy shape ``com.amazonaws.workmail#Member``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.entity_state
    import capo_workmail.types.member_type
    import capo_workmail.types.string
    import capo_workmail.types.timestamp


class Member(TypedDict, closed=True):
    id: NotRequired["capo_workmail.types.string.String"]
    """<p>The identifier of the member.</p>"""
    name: NotRequired["capo_workmail.types.string.String"]
    """<p>The name of the member.</p>"""
    type: NotRequired["capo_workmail.types.member_type.MemberType"]
    """<p>A member can be a user or group.</p>"""
    state: NotRequired["capo_workmail.types.entity_state.EntityState"]
    """<p>The state of the member, which can be ENABLED, DISABLED, or DELETED.</p>"""
    enabled_date: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date indicating when the member was enabled for WorkMail use.</p>"""
    disabled_date: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date indicating when the member was disabled from WorkMail use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Member) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_workmail.types.member_type

        out["Type"] = capo_workmail.types.member_type.serialize_aws_json_1_1(
            value["type"]
        )
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


def deserialize_aws_json_1_1(data: dict) -> Member:
    out: Member = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import capo_workmail.types.member_type

        out["type"] = capo_workmail.types.member_type.deserialize_aws_json_1_1(
            data["Type"]
        )
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
