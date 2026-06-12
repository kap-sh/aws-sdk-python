"""Generated from Smithy shape ``com.amazonaws.ecr#RegistryScanningRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.registry_scanning_rule

RegistryScanningRuleList: TypeAlias = list[
    "aws_sdk_ecr.types.registry_scanning_rule.RegistryScanningRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistryScanningRuleList) -> list:
    import aws_sdk_ecr.types.registry_scanning_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecr.types.registry_scanning_rule.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RegistryScanningRuleList:
    import aws_sdk_ecr.types.registry_scanning_rule

    out: RegistryScanningRuleList = []
    for item in data:
        out.append(
            aws_sdk_ecr.types.registry_scanning_rule.deserialize_aws_json_1_1(item)
        )
    return out
