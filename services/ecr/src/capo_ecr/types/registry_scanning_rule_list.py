"""Generated from Smithy shape ``com.amazonaws.ecr#RegistryScanningRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.registry_scanning_rule

RegistryScanningRuleList: TypeAlias = list[
    "capo_ecr.types.registry_scanning_rule.RegistryScanningRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistryScanningRuleList) -> list:
    import capo_ecr.types.registry_scanning_rule

    out: list = []
    for item in value:
        out.append(capo_ecr.types.registry_scanning_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RegistryScanningRuleList:
    import capo_ecr.types.registry_scanning_rule

    out: RegistryScanningRuleList = []
    for item in data:
        out.append(capo_ecr.types.registry_scanning_rule.deserialize_aws_json_1_1(item))
    return out
