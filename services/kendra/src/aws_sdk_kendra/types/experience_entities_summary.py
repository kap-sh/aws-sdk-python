"""Generated from Smithy shape ``com.amazonaws.kendra#ExperienceEntitiesSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.entity_display_data
    import aws_sdk_kendra.types.entity_id
    import aws_sdk_kendra.types.entity_type


class ExperienceEntitiesSummary(TypedDict):
    entity_id: NotRequired["aws_sdk_kendra.types.entity_id.EntityId"]
    """<p>The identifier of a user or group in your IAM Identity Center identity source. For example, a user ID could be an email.</p>"""
    entity_type: NotRequired["aws_sdk_kendra.types.entity_type.EntityType"]
    """<p>Shows the type as <code>User</code> or <code>Group</code>.</p>"""
    display_data: NotRequired[
        "aws_sdk_kendra.types.entity_display_data.EntityDisplayData"
    ]
    """<p>Information about the user entity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExperienceEntitiesSummary) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "entity_type" in value:
        import aws_sdk_kendra.types.entity_type

        out["EntityType"] = aws_sdk_kendra.types.entity_type.serialize_aws_json_1_1(
            value["entity_type"]
        )
    if "display_data" in value:
        import aws_sdk_kendra.types.entity_display_data

        out["DisplayData"] = (
            aws_sdk_kendra.types.entity_display_data.serialize_aws_json_1_1(
                value["display_data"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExperienceEntitiesSummary:
    out: ExperienceEntitiesSummary = {}  # type: ignore[typeddict-item]
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    if "EntityType" in data:
        import aws_sdk_kendra.types.entity_type

        out["entity_type"] = aws_sdk_kendra.types.entity_type.deserialize_aws_json_1_1(
            data["EntityType"]
        )
    if "DisplayData" in data:
        import aws_sdk_kendra.types.entity_display_data

        out["display_data"] = (
            aws_sdk_kendra.types.entity_display_data.deserialize_aws_json_1_1(
                data["DisplayData"]
            )
        )
    return out
