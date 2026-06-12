"""Generated from Smithy shape ``com.amazonaws.fms#OrderedRemediationActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.remediation_action_with_order

OrderedRemediationActions: TypeAlias = list[
    "aws_sdk_fms.types.remediation_action_with_order.RemediationActionWithOrder"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrderedRemediationActions) -> list:
    import aws_sdk_fms.types.remediation_action_with_order

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fms.types.remediation_action_with_order.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OrderedRemediationActions:
    import aws_sdk_fms.types.remediation_action_with_order

    out: OrderedRemediationActions = []
    for item in data:
        out.append(
            aws_sdk_fms.types.remediation_action_with_order.deserialize_aws_json_1_1(
                item
            )
        )
    return out
