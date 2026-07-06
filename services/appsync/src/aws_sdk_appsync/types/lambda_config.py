"""Generated from Smithy shape ``com.amazonaws.appsync#LambdaConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.invoke_type


class LambdaConfig(TypedDict, closed=True):
    invoke_type: NotRequired["aws_sdk_appsync.types.invoke_type.InvokeType"]
    """<p>The invocation type for a Lambda data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaConfig) -> dict:
    out: dict = {}
    if "invoke_type" in value:
        import aws_sdk_appsync.types.invoke_type

        out["invokeType"] = aws_sdk_appsync.types.invoke_type.serialize_json(
            value["invoke_type"]
        )
    return out


def deserialize_json(data: dict) -> LambdaConfig:
    out: LambdaConfig = {}  # type: ignore[typeddict-item]
    if "invokeType" in data:
        import aws_sdk_appsync.types.invoke_type

        out["invoke_type"] = aws_sdk_appsync.types.invoke_type.deserialize_json(
            data["invokeType"]
        )
    return out
