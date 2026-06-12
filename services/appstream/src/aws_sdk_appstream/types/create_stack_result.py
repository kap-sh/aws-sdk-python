"""Generated from Smithy shape ``com.amazonaws.appstream#CreateStackResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.stack


class CreateStackResult(TypedDict):
    stack: NotRequired["aws_sdk_appstream.types.stack.Stack"]
    """<p>Information about the stack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStackResult) -> dict:
    out: dict = {}
    if "stack" in value:
        import aws_sdk_appstream.types.stack

        out["Stack"] = aws_sdk_appstream.types.stack.serialize_aws_json_1_1(
            value["stack"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStackResult:
    out: CreateStackResult = {}  # type: ignore[typeddict-item]
    if "Stack" in data:
        import aws_sdk_appstream.types.stack

        out["stack"] = aws_sdk_appstream.types.stack.deserialize_aws_json_1_1(
            data["Stack"]
        )
    return out
