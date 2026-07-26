"""Generated from Smithy shape ``com.amazonaws.cloud9#EnvironmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloud9.types.environment

EnvironmentList: TypeAlias = list["capo_cloud9.types.environment.Environment"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentList) -> list:
    import capo_cloud9.types.environment

    out: list = []
    for item in value:
        out.append(capo_cloud9.types.environment.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EnvironmentList:
    import capo_cloud9.types.environment

    out: EnvironmentList = []
    for item in data:
        out.append(capo_cloud9.types.environment.deserialize_aws_json_1_1(item))
    return out
