"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdMappingTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.collaboration_arn
    import aws_sdk_cleanrooms.types.id_mapping_table_arn
    import aws_sdk_cleanrooms.types.id_mapping_table_input_reference_config
    import aws_sdk_cleanrooms.types.id_mapping_table_input_reference_properties
    import aws_sdk_cleanrooms.types.kms_key_arn
    import aws_sdk_cleanrooms.types.membership_arn
    import aws_sdk_cleanrooms.types.resource_alias
    import aws_sdk_cleanrooms.types.resource_description
    import aws_sdk_cleanrooms.types.uuid


class IdMappingTable(TypedDict, closed=True):
    id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the ID mapping table.</p>"""
    arn: "aws_sdk_cleanrooms.types.id_mapping_table_arn.IdMappingTableArn"
    """<p>The Amazon Resource Name (ARN) of the ID mapping table.</p>"""
    input_reference_config: "aws_sdk_cleanrooms.types.id_mapping_table_input_reference_config.IdMappingTableInputReferenceConfig"
    """<p>The input reference configuration for the ID mapping table.</p>"""
    membership_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the membership resource for the ID mapping table.</p>"""
    membership_arn: "aws_sdk_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The Amazon Resource Name (ARN) of the membership resource for the ID mapping table.</p>"""
    collaboration_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the collaboration that contains this ID mapping table.</p>"""
    collaboration_arn: "aws_sdk_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The Amazon Resource Name (ARN) of the collaboration that contains this ID mapping table.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the ID mapping table.</p>"""
    name: "aws_sdk_cleanrooms.types.resource_alias.ResourceAlias"
    """<p>The name of the ID mapping table.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the ID mapping table was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the ID mapping table was updated.</p>"""
    input_reference_properties: "aws_sdk_cleanrooms.types.id_mapping_table_input_reference_properties.IdMappingTableInputReferenceProperties"
    """<p>The input reference properties for the ID mapping table.</p>"""
    kms_key_arn: NotRequired["aws_sdk_cleanrooms.types.kms_key_arn.KMSKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services KMS key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingTable) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import aws_sdk_cleanrooms.types.id_mapping_table_input_reference_config

    out["inputReferenceConfig"] = (
        aws_sdk_cleanrooms.types.id_mapping_table_input_reference_config.serialize_json(
            value["input_reference_config"]
        )
    )
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    if "description" in value:
        out["description"] = value["description"]
    out["name"] = value["name"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    import aws_sdk_cleanrooms.types.id_mapping_table_input_reference_properties

    out["inputReferenceProperties"] = (
        aws_sdk_cleanrooms.types.id_mapping_table_input_reference_properties.serialize_json(
            value["input_reference_properties"]
        )
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> IdMappingTable:
    out: IdMappingTable = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("IdMappingTable.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IdMappingTable.arn required")
    if "inputReferenceConfig" in data:
        import aws_sdk_cleanrooms.types.id_mapping_table_input_reference_config

        out["input_reference_config"] = (
            aws_sdk_cleanrooms.types.id_mapping_table_input_reference_config.deserialize_json(
                data["inputReferenceConfig"]
            )
        )
    else:
        raise DeserializationError("IdMappingTable.input_reference_config required")
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("IdMappingTable.membership_id required")
    if "membershipArn" in data:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError("IdMappingTable.membership_arn required")
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError("IdMappingTable.collaboration_id required")
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError("IdMappingTable.collaboration_arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("IdMappingTable.name required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("IdMappingTable.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("IdMappingTable.update_time required")
    if "inputReferenceProperties" in data:
        import aws_sdk_cleanrooms.types.id_mapping_table_input_reference_properties

        out["input_reference_properties"] = (
            aws_sdk_cleanrooms.types.id_mapping_table_input_reference_properties.deserialize_json(
                data["inputReferenceProperties"]
            )
        )
    else:
        raise DeserializationError("IdMappingTable.input_reference_properties required")
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
