"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAssociationAnalysisRule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type
    import aws_sdk_cleanrooms.types.configured_table_association_arn
    import aws_sdk_cleanrooms.types.configured_table_association_identifier
    import aws_sdk_cleanrooms.types.membership_identifier


class ConfiguredTableAssociationAnalysisRule(TypedDict):
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p> The membership identifier for the configured table association analysis rule.</p>"""
    configured_table_association_id: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier"
    """<p> The unique identifier for the configured table association.</p>"""
    configured_table_association_arn: "aws_sdk_cleanrooms.types.configured_table_association_arn.ConfiguredTableAssociationArn"
    """<p> The Amazon Resource Name (ARN) of the configured table association.</p>"""
    policy: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy.ConfiguredTableAssociationAnalysisRulePolicy"
    """<p> The policy of the configured table association analysis rule.</p>"""
    type: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType"
    """<p> The type of the configured table association analysis rule.</p>"""
    create_time: "datetime.datetime"
    """<p> The creation time of the configured table association analysis rule.</p>"""
    update_time: "datetime.datetime"
    """<p> The update time of the configured table association analysis rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAssociationAnalysisRule) -> dict:
    out: dict = {}
    out["membershipIdentifier"] = value["membership_identifier"]
    out["configuredTableAssociationId"] = value["configured_table_association_id"]
    out["configuredTableAssociationArn"] = value["configured_table_association_arn"]
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy

    out["policy"] = (
        aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy.serialize_json(
            value["policy"]
        )
    )
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type

    out["type"] = (
        aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type.serialize_json(
            value["type"]
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


def deserialize_json(data: dict) -> ConfiguredTableAssociationAnalysisRule:
    out: ConfiguredTableAssociationAnalysisRule = {}  # type: ignore[typeddict-item]
    if "membershipIdentifier" in data:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        raise DeserializationError(
            "ConfiguredTableAssociationAnalysisRule.membership_identifier required"
        )
    if "configuredTableAssociationId" in data:
        out["configured_table_association_id"] = data["configuredTableAssociationId"]
    else:
        raise DeserializationError(
            "ConfiguredTableAssociationAnalysisRule.configured_table_association_id required"
        )
    if "configuredTableAssociationArn" in data:
        out["configured_table_association_arn"] = data["configuredTableAssociationArn"]
    else:
        raise DeserializationError(
            "ConfiguredTableAssociationAnalysisRule.configured_table_association_arn required"
        )
    if "policy" in data:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy

        out["policy"] = (
            aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy.deserialize_json(
                data["policy"]
            )
        )
    else:
        raise DeserializationError(
            "ConfiguredTableAssociationAnalysisRule.policy required"
        )
    if "type" in data:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type

        out["type"] = (
            aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError(
            "ConfiguredTableAssociationAnalysisRule.type required"
        )
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "ConfiguredTableAssociationAnalysisRule.create_time required"
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
            "ConfiguredTableAssociationAnalysisRule.update_time required"
        )
    return out
