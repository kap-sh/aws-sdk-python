"""Generated from Smithy shape ``com.amazonaws.fms#PossibleRemediationActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.possible_remediation_action

PossibleRemediationActionList: TypeAlias = list[
    "aws_sdk_fms.types.possible_remediation_action.PossibleRemediationAction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PossibleRemediationActionList) -> list:
    import aws_sdk_fms.types.possible_remediation_action

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fms.types.possible_remediation_action.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PossibleRemediationActionList:
    import aws_sdk_fms.types.possible_remediation_action

    out: PossibleRemediationActionList = []
    for item in data:
        out.append(
            aws_sdk_fms.types.possible_remediation_action.deserialize_aws_json_1_1(item)
        )
    return out
