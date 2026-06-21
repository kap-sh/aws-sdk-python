"""Generated from Smithy shape ``com.amazonaws.sagemaker#StudioLifecycleConfigAppType``."""

from typing import Literal, TypeAlias, cast

StudioLifecycleConfigAppType: TypeAlias = Literal[
    "JupyterServer",
    "KernelGateway",
    "CodeEditor",
    "JupyterLab",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StudioLifecycleConfigAppType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StudioLifecycleConfigAppType:
    return cast(StudioLifecycleConfigAppType, data)
