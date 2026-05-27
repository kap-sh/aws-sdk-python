"""Generated from Smithy shape ``com.amazonaws.lambda#ImageConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string_list
    import aws_sdk_lambda.types.working_directory


class ImageConfig(TypedDict):
    entry_point: NotRequired["aws_sdk_lambda.types.string_list.StringList"]
    """<p>Specifies the entry point to their application, which is typically the location of the runtime executable.</p>"""
    command: NotRequired["aws_sdk_lambda.types.string_list.StringList"]
    """<p>Specifies parameters that you want to pass in with ENTRYPOINT.</p>"""
    working_directory: NotRequired[
        "aws_sdk_lambda.types.working_directory.WorkingDirectory"
    ]
    """<p>Specifies the working directory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageConfig) -> dict:
    out: dict = {}
    if "entry_point" in value:
        import aws_sdk_lambda.types.string_list

        out["EntryPoint"] = aws_sdk_lambda.types.string_list.serialize_json(
            value["entry_point"]
        )
    if "command" in value:
        import aws_sdk_lambda.types.string_list

        out["Command"] = aws_sdk_lambda.types.string_list.serialize_json(
            value["command"]
        )
    if "working_directory" in value:
        out["WorkingDirectory"] = value["working_directory"]
    return out


def deserialize_json(data: dict) -> ImageConfig:
    out: ImageConfig = {}  # type: ignore[typeddict-item]
    if "EntryPoint" in data:
        import aws_sdk_lambda.types.string_list

        out["entry_point"] = aws_sdk_lambda.types.string_list.deserialize_json(
            data["EntryPoint"]
        )
    if "Command" in data:
        import aws_sdk_lambda.types.string_list

        out["command"] = aws_sdk_lambda.types.string_list.deserialize_json(
            data["Command"]
        )
    if "WorkingDirectory" in data:
        out["working_directory"] = data["WorkingDirectory"]
    return out
