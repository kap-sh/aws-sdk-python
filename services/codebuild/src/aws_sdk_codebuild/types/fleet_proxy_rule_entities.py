"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetProxyRuleEntities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.string

FleetProxyRuleEntities: TypeAlias = list["aws_sdk_codebuild.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetProxyRuleEntities) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FleetProxyRuleEntities:
    return list(data)
