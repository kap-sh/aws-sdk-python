"""Generated from Smithy shape ``com.amazonaws.apprunner#Runtime``."""

from typing import Literal, TypeAlias, cast

Runtime: TypeAlias = Literal[
    "PYTHON_3",
    "NODEJS_12",
    "NODEJS_14",
    "CORRETTO_8",
    "CORRETTO_11",
    "NODEJS_16",
    "GO_1",
    "DOTNET_6",
    "PHP_81",
    "RUBY_31",
    "PYTHON_311",
    "NODEJS_18",
    "NODEJS_22",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Runtime) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Runtime:
    return cast(Runtime, data)
