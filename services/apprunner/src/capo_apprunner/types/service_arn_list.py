"""Generated from Smithy shape ``com.amazonaws.apprunner#ServiceArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn

ServiceArnList: TypeAlias = list[
    "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceArnList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ServiceArnList:
    return list(data)
