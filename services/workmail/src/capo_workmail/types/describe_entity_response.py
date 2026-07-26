"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeEntityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.entity_type
    import capo_workmail.types.string
    import capo_workmail.types.work_mail_identifier


class DescribeEntityResponse(TypedDict, closed=True):
    entity_id: NotRequired[
        "capo_workmail.types.work_mail_identifier.WorkMailIdentifier"
    ]
    """<p>The entity ID under which the entity exists.</p>"""
    name: NotRequired["capo_workmail.types.string.String"]
    """<p>Username, GroupName, or ResourceName based on entity type.</p>"""
    type: NotRequired["capo_workmail.types.entity_type.EntityType"]
    """<p>Entity type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEntityResponse) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_workmail.types.entity_type

        out["Type"] = capo_workmail.types.entity_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEntityResponse:
    out: DescribeEntityResponse = {}  # type: ignore[typeddict-item]
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import capo_workmail.types.entity_type

        out["type"] = capo_workmail.types.entity_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out
