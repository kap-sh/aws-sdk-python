"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppType``."""

from typing import Literal, TypeAlias, cast

AppType: TypeAlias = Literal[
    "JupyterServer",
    "KernelGateway",
    "DetailedProfiler",
    "TensorBoard",
    "CodeEditor",
    "JupyterLab",
    "RStudioServerPro",
    "RSessionGateway",
    "Canvas",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppType:
    return cast(AppType, data)
