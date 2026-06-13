"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAssociationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type_list
    import aws_sdk_cleanrooms.types.configured_table_association_arn
    import aws_sdk_cleanrooms.types.membership_arn
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.table_alias
    import aws_sdk_cleanrooms.types.uuid


class ConfiguredTableAssociationSummary(TypedDict):
    configured_table_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique configured table ID that this configured table association refers to.</p>"""
    membership_id: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    """<p>The unique ID for the membership that the configured table association belongs to.</p>"""
    membership_arn: "aws_sdk_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The unique ARN for the membership that the configured table association belongs to.</p>"""
    name: "aws_sdk_cleanrooms.types.table_alias.TableAlias"
    """<p>The name of the configured table association. The table is identified by this name when running Protected Queries against the underlying data.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the configured table association was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the configured table association was last updated.</p>"""
    id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the configured table association.</p>"""
    arn: "aws_sdk_cleanrooms.types.configured_table_association_arn.ConfiguredTableAssociationArn"
    """<p>The unique ARN for the configured table association.</p>"""
    analysis_rule_types: NotRequired[
        "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type_list.ConfiguredTableAssociationAnalysisRuleTypeList"
    ]
    """<p>The analysis rule types that are associated with the configured table associations in this summary. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAssociationSummary) -> dict:
    out: dict = {}
    out["configuredTableId"] = value["configured_table_id"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    out["name"] = value["name"]
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
    if "analysis_rule_types" in value:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type_list

        out["analysisRuleTypes"] = (
            aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type_list.serialize_json(
                value["analysis_rule_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfiguredTableAssociationSummary:
    out: ConfiguredTableAssociationSummary = {}  # type: ignore[typeddict-item]
    if "configuredTableId" in data:
        out["configured_table_id"] = data["configuredTableId"]
    else:
        raise DeserializationError(
            "ConfiguredTableAssociationSummary.configured_table_id required"
        )
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError(
            "ConfiguredTableAssociationSummary.membership_id required"
        )
    if "membershipArn" in data:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError(
            "ConfiguredTableAssociationSummary.membership_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConfiguredTableAssociationSummary.name required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "ConfiguredTableAssociationSummary.create_time required"
        )
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError(
            "ConfiguredTableAssociationSummary.update_time required"
        )
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ConfiguredTableAssociationSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ConfiguredTableAssociationSummary.arn required")
    if "analysisRuleTypes" in data:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type_list

        out["analysis_rule_types"] = (
            aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type_list.deserialize_json(
                data["analysisRuleTypes"]
            )
        )
    return out
