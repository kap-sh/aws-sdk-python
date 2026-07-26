"""Generated from Smithy shape ``com.amazonaws.workmail#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.email_address
    import capo_workmail.types.entity_state
    import capo_workmail.types.resource_description
    import capo_workmail.types.resource_name
    import capo_workmail.types.resource_type
    import capo_workmail.types.timestamp
    import capo_workmail.types.work_mail_identifier


class Resource(TypedDict, closed=True):
    id: NotRequired["capo_workmail.types.work_mail_identifier.WorkMailIdentifier"]
    """<p>The identifier of the resource.</p>"""
    email: NotRequired["capo_workmail.types.email_address.EmailAddress"]
    """<p>The email of the resource.</p>"""
    name: NotRequired["capo_workmail.types.resource_name.ResourceName"]
    """<p>The name of the resource.</p>"""
    type: NotRequired["capo_workmail.types.resource_type.ResourceType"]
    """<p>The type of the resource: equipment or room.</p>"""
    state: NotRequired["capo_workmail.types.entity_state.EntityState"]
    """<p>The state of the resource, which can be ENABLED, DISABLED, or DELETED.</p>"""
    enabled_date: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date indicating when the resource was enabled for WorkMail use.</p>"""
    disabled_date: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date indicating when the resource was disabled from WorkMail use.</p>"""
    description: NotRequired[
        "capo_workmail.types.resource_description.ResourceDescription"
    ]
    """<p>Resource description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Resource) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "email" in value:
        out["Email"] = value["email"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_workmail.types.resource_type

        out["Type"] = capo_workmail.types.resource_type.serialize_aws_json_1_1(
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
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Email" in data:
        out["email"] = data["Email"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import capo_workmail.types.resource_type

        out["type"] = capo_workmail.types.resource_type.deserialize_aws_json_1_1(
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
    if "Description" in data:
        out["description"] = data["Description"]
    return out
