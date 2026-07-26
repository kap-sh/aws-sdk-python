"""Generated from Smithy shape ``com.amazonaws.lightsail#SetupExecutionDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.setup_execution_details

SetupExecutionDetailsList: TypeAlias = list[
    "capo_lightsail.types.setup_execution_details.SetupExecutionDetails"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetupExecutionDetailsList) -> list:
    import capo_lightsail.types.setup_execution_details

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.setup_execution_details.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SetupExecutionDetailsList:
    import capo_lightsail.types.setup_execution_details

    out: SetupExecutionDetailsList = []
    for item in data:
        out.append(
            capo_lightsail.types.setup_execution_details.deserialize_aws_json_1_1(item)
        )
    return out
