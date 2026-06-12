"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "JupyterServer",
        "KernelGateway",
        "DetailedProfiler",
        "TensorBoard",
        "CodeEditor",
        "JupyterLab",
        "RStudioServerPro",
        "RSessionGateway",
        "Canvas",
    )
)


def serialize_aws_json_1_1(value: AppType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppType value: {data!r}")
    return cast(AppType, data)
