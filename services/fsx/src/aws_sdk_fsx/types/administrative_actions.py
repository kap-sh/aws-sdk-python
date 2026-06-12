"""Generated from Smithy shape ``com.amazonaws.fsx#AdministrativeActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.administrative_action

AdministrativeActions: TypeAlias = list[
    "aws_sdk_fsx.types.administrative_action.AdministrativeAction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdministrativeActions) -> list:
    import aws_sdk_fsx.types.administrative_action

    out: list = []
    for item in value:
        out.append(aws_sdk_fsx.types.administrative_action.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AdministrativeActions:
    import aws_sdk_fsx.types.administrative_action

    out: AdministrativeActions = []
    for item in data:
        out.append(
            aws_sdk_fsx.types.administrative_action.deserialize_aws_json_1_1(item)
        )
    return out
