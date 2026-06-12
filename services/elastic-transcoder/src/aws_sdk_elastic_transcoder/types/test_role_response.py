"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#TestRoleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.exception_messages
    import aws_sdk_elastic_transcoder.types.success


class TestRoleResponse(TypedDict):
    success: NotRequired["aws_sdk_elastic_transcoder.types.success.Success"]
    """<p>If the operation is successful, this value is <code>true</code>; otherwise, the value is <code>false</code>.</p>"""
    messages: NotRequired[
        "aws_sdk_elastic_transcoder.types.exception_messages.ExceptionMessages"
    ]
    """<p>If the <code>Success</code> element contains <code>false</code>, this value is an array of one or more error messages that were generated during the test process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRoleResponse) -> dict:
    out: dict = {}
    if "success" in value:
        out["Success"] = value["success"]
    if "messages" in value:
        import aws_sdk_elastic_transcoder.types.exception_messages

        out["Messages"] = (
            aws_sdk_elastic_transcoder.types.exception_messages.serialize_json(
                value["messages"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestRoleResponse:
    out: TestRoleResponse = {}  # type: ignore[typeddict-item]
    if "Success" in data:
        out["success"] = data["Success"]
    if "Messages" in data:
        import aws_sdk_elastic_transcoder.types.exception_messages

        out["messages"] = (
            aws_sdk_elastic_transcoder.types.exception_messages.deserialize_json(
                data["Messages"]
            )
        )
    return out
