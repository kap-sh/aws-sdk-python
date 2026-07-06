"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdMappingTableSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.collaboration_arn
    import aws_sdk_cleanrooms.types.id_mapping_table_arn
    import aws_sdk_cleanrooms.types.id_mapping_table_input_reference_config
    import aws_sdk_cleanrooms.types.membership_arn
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.resource_alias
    import aws_sdk_cleanrooms.types.resource_description
    import aws_sdk_cleanrooms.types.uuid


class IdMappingTableSummary(TypedDict, closed=True):
    collaboration_arn: "aws_sdk_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The Amazon Resource Name (ARN) of the collaboration that contains this ID mapping table.</p>"""
    collaboration_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the collaboration that contains this ID mapping table.</p>"""
    membership_id: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    """<p>The unique identifier of the membership resource for this ID mapping table.</p>"""
    membership_arn: "aws_sdk_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The Amazon Resource Name (ARN) of the membership resource for this ID mapping table.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which this ID mapping table was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which this ID mapping table was updated.</p>"""
    id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of this ID mapping table.</p>"""
    arn: "aws_sdk_cleanrooms.types.id_mapping_table_arn.IdMappingTableArn"
    """<p>The Amazon Resource Name (ARN) of this ID mapping table.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of this ID mapping table.</p>"""
    input_reference_config: "aws_sdk_cleanrooms.types.id_mapping_table_input_reference_config.IdMappingTableInputReferenceConfig"
    """<p>The input reference configuration for the ID mapping table.</p>"""
    name: "aws_sdk_cleanrooms.types.resource_alias.ResourceAlias"
    """<p>The name of this ID mapping table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingTableSummary) -> dict:
    out: dict = {}
    out["collaborationArn"] = value["collaboration_arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_cleanrooms.types.id_mapping_table_input_reference_config

    out["inputReferenceConfig"] = (
        aws_sdk_cleanrooms.types.id_mapping_table_input_reference_config.serialize_json(
            value["input_reference_config"]
        )
    )
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> IdMappingTableSummary:
    out: IdMappingTableSummary = {}  # type: ignore[typeddict-item]
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError("IdMappingTableSummary.collaboration_arn required")
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError("IdMappingTableSummary.collaboration_id required")
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("IdMappingTableSummary.membership_id required")
    if "membershipArn" in data:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError("IdMappingTableSummary.membership_arn required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("IdMappingTableSummary.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("IdMappingTableSummary.update_time required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("IdMappingTableSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IdMappingTableSummary.arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "inputReferenceConfig" in data:
        import aws_sdk_cleanrooms.types.id_mapping_table_input_reference_config

        out["input_reference_config"] = (
            aws_sdk_cleanrooms.types.id_mapping_table_input_reference_config.deserialize_json(
                data["inputReferenceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "IdMappingTableSummary.input_reference_config required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("IdMappingTableSummary.name required")
    return out
