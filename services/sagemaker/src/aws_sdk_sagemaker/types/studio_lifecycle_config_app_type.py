"""Generated from Smithy shape ``com.amazonaws.sagemaker#StudioLifecycleConfigAppType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

StudioLifecycleConfigAppType: TypeAlias = Literal[
    "JupyterServer",
    "KernelGateway",
    "CodeEditor",
    "JupyterLab",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JupyterServer",
        "KernelGateway",
        "CodeEditor",
        "JupyterLab",
    )
)


def serialize_aws_json_1_1(value: StudioLifecycleConfigAppType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StudioLifecycleConfigAppType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StudioLifecycleConfigAppType value: {data!r}"
        )
    return cast(StudioLifecycleConfigAppType, data)
