"""Generated from Smithy shape ``com.amazonaws.workmail#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmail.types.email_address
    import aws_sdk_workmail.types.entity_state
    import aws_sdk_workmail.types.resource_description
    import aws_sdk_workmail.types.resource_name
    import aws_sdk_workmail.types.resource_type
    import aws_sdk_workmail.types.timestamp
    import aws_sdk_workmail.types.work_mail_identifier


class Resource(TypedDict, closed=True):
    id: NotRequired["aws_sdk_workmail.types.work_mail_identifier.WorkMailIdentifier"]
    """<p>The identifier of the resource.</p>"""
    email: NotRequired["aws_sdk_workmail.types.email_address.EmailAddress"]
    """<p>The email of the resource.</p>"""
    name: NotRequired["aws_sdk_workmail.types.resource_name.ResourceName"]
    """<p>The name of the resource.</p>"""
    type: NotRequired["aws_sdk_workmail.types.resource_type.ResourceType"]
    """<p>The type of the resource: equipment or room.</p>"""
    state: NotRequired["aws_sdk_workmail.types.entity_state.EntityState"]
    """<p>The state of the resource, which can be ENABLED, DISABLED, or DELETED.</p>"""
    enabled_date: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p>The date indicating when the resource was enabled for WorkMail use.</p>"""
    disabled_date: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p>The date indicating when the resource was disabled from WorkMail use.</p>"""
    description: NotRequired[
        "aws_sdk_workmail.types.resource_description.ResourceDescription"
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
        import aws_sdk_workmail.types.resource_type

        out["Type"] = aws_sdk_workmail.types.resource_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "state" in value:
        import aws_sdk_workmail.types.entity_state

        out["State"] = aws_sdk_workmail.types.entity_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "enabled_date" in value:
        import aws_sdk_workmail.types.timestamp

        out["EnabledDate"] = aws_sdk_workmail.types.timestamp.serialize_aws_json_1_1(
            value["enabled_date"]
        )
    if "disabled_date" in value:
        import aws_sdk_workmail.types.timestamp

        out["DisabledDate"] = aws_sdk_workmail.types.timestamp.serialize_aws_json_1_1(
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
        import aws_sdk_workmail.types.resource_type

        out["type"] = aws_sdk_workmail.types.resource_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "State" in data:
        import aws_sdk_workmail.types.entity_state

        out["state"] = aws_sdk_workmail.types.entity_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "EnabledDate" in data:
        import aws_sdk_workmail.types.timestamp

        out["enabled_date"] = aws_sdk_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["EnabledDate"]
        )
    if "DisabledDate" in data:
        import aws_sdk_workmail.types.timestamp

        out["disabled_date"] = (
            aws_sdk_workmail.types.timestamp.deserialize_aws_json_1_1(
                data["DisabledDate"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
