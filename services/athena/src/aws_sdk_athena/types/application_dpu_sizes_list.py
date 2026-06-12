"""Generated from Smithy shape ``com.amazonaws.athena#ApplicationDPUSizesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.application_dpu_sizes

ApplicationDPUSizesList: TypeAlias = list[
    "aws_sdk_athena.types.application_dpu_sizes.ApplicationDPUSizes"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationDPUSizesList) -> list:
    import aws_sdk_athena.types.application_dpu_sizes

    out: list = []
    for item in value:
        out.append(
            aws_sdk_athena.types.application_dpu_sizes.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationDPUSizesList:
    import aws_sdk_athena.types.application_dpu_sizes

    out: ApplicationDPUSizesList = []
    for item in data:
        out.append(
            aws_sdk_athena.types.application_dpu_sizes.deserialize_aws_json_1_1(item)
        )
    return out
