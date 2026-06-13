"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAnalysisRule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule_type
    import aws_sdk_cleanrooms.types.configured_table_arn
    import aws_sdk_cleanrooms.types.uuid


class ConfiguredTableAnalysisRule(TypedDict):
    configured_table_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the configured table.</p>"""
    configured_table_arn: (
        "aws_sdk_cleanrooms.types.configured_table_arn.ConfiguredTableArn"
    )
    """<p>The unique ARN for the configured table.</p>"""
    policy: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy.ConfiguredTableAnalysisRulePolicy"
    """<p>The policy that controls SQL query rules.</p>"""
    type: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType"
    """<p>The type of configured table analysis rule.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the configured table analysis rule was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the configured table analysis rule was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAnalysisRule) -> dict:
    out: dict = {}
    out["configuredTableId"] = value["configured_table_id"]
    out["configuredTableArn"] = value["configured_table_arn"]
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy

    out["policy"] = (
        aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy.serialize_json(
            value["policy"]
        )
    )
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule_type

    out["type"] = (
        aws_sdk_cleanrooms.types.configured_table_analysis_rule_type.serialize_json(
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


def deserialize_json(data: dict) -> ConfiguredTableAnalysisRule:
    out: ConfiguredTableAnalysisRule = {}  # type: ignore[typeddict-item]
    if "configuredTableId" in data:
        out["configured_table_id"] = data["configuredTableId"]
    else:
        raise DeserializationError(
            "ConfiguredTableAnalysisRule.configured_table_id required"
        )
    if "configuredTableArn" in data:
        out["configured_table_arn"] = data["configuredTableArn"]
    else:
        raise DeserializationError(
            "ConfiguredTableAnalysisRule.configured_table_arn required"
        )
    if "policy" in data:
        import aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy

        out["policy"] = (
            aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy.deserialize_json(
                data["policy"]
            )
        )
    else:
        raise DeserializationError("ConfiguredTableAnalysisRule.policy required")
    if "type" in data:
        import aws_sdk_cleanrooms.types.configured_table_analysis_rule_type

        out["type"] = (
            aws_sdk_cleanrooms.types.configured_table_analysis_rule_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("ConfiguredTableAnalysisRule.type required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("ConfiguredTableAnalysisRule.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("ConfiguredTableAnalysisRule.update_time required")
    return out
