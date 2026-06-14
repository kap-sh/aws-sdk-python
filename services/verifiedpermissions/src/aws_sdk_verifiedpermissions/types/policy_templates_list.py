"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyTemplatesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.policy_template_item

PolicyTemplatesList: TypeAlias = list[
    "aws_sdk_verifiedpermissions.types.policy_template_item.PolicyTemplateItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyTemplatesList) -> list:
    import aws_sdk_verifiedpermissions.types.policy_template_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_verifiedpermissions.types.policy_template_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PolicyTemplatesList:
    import aws_sdk_verifiedpermissions.types.policy_template_item

    out: PolicyTemplatesList = []
    for item in data:
        out.append(
            aws_sdk_verifiedpermissions.types.policy_template_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
