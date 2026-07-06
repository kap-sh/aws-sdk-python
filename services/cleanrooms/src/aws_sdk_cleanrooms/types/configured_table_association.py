"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.configured_table_arn
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type_list
    import aws_sdk_cleanrooms.types.configured_table_association_arn
    import aws_sdk_cleanrooms.types.membership_arn
    import aws_sdk_cleanrooms.types.role_arn
    import aws_sdk_cleanrooms.types.table_alias
    import aws_sdk_cleanrooms.types.table_description
    import aws_sdk_cleanrooms.types.uuid


class ConfiguredTableAssociation(TypedDict, closed=True):
    arn: "aws_sdk_cleanrooms.types.configured_table_association_arn.ConfiguredTableAssociationArn"
    """<p>The unique ARN for the configured table association.</p>"""
    id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the configured table association.</p>"""
    configured_table_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the configured table that the association refers to.</p>"""
    configured_table_arn: (
        "aws_sdk_cleanrooms.types.configured_table_arn.ConfiguredTableArn"
    )
    """<p>The unique ARN for the configured table that the association refers to.</p>"""
    membership_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the membership this configured table association belongs to.</p>"""
    membership_arn: "aws_sdk_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The unique ARN for the membership this configured table association belongs to.</p>"""
    role_arn: "aws_sdk_cleanrooms.types.role_arn.RoleArn"
    """<p>The service will assume this role to access catalog metadata and query the table.</p>"""
    name: "aws_sdk_cleanrooms.types.table_alias.TableAlias"
    """<p>The name of the configured table association, in lowercase. The table is identified by this name when running protected queries against the underlying data.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.table_description.TableDescription"
    ]
    """<p>A description of the configured table association.</p>"""
    analysis_rule_types: NotRequired[
        "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type_list.ConfiguredTableAssociationAnalysisRuleTypeList"
    ]
    """<p> The analysis rule types for the configured table association.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the configured table association was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the configured table association was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAssociation) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    out["configuredTableId"] = value["configured_table_id"]
    out["configuredTableArn"] = value["configured_table_arn"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    out["roleArn"] = value["role_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "analysis_rule_types" in value:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type_list

        out["analysisRuleTypes"] = (
            aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type_list.serialize_json(
                value["analysis_rule_types"]
            )
        )
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> ConfiguredTableAssociation:
    out: ConfiguredTableAssociation = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ConfiguredTableAssociation.arn required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ConfiguredTableAssociation.id required")
    if "configuredTableId" in data:
        out["configured_table_id"] = data["configuredTableId"]
    else:
        raise DeserializationError(
            "ConfiguredTableAssociation.configured_table_id required"
        )
    if "configuredTableArn" in data:
        out["configured_table_arn"] = data["configuredTableArn"]
    else:
        raise DeserializationError(
            "ConfiguredTableAssociation.configured_table_arn required"
        )
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("ConfiguredTableAssociation.membership_id required")
    if "membershipArn" in data:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError("ConfiguredTableAssociation.membership_arn required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("ConfiguredTableAssociation.role_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConfiguredTableAssociation.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "analysisRuleTypes" in data:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type_list

        out["analysis_rule_types"] = (
            aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type_list.deserialize_json(
                data["analysisRuleTypes"]
            )
        )
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("ConfiguredTableAssociation.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("ConfiguredTableAssociation.update_time required")
    return out
