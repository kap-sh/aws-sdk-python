"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#TestRoleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.exception_messages
    import capo_elastic_transcoder.types.success


class TestRoleResponse(TypedDict, closed=True):
    success: NotRequired["capo_elastic_transcoder.types.success.Success"]
    """<p>If the operation is successful, this value is <code>true</code>; otherwise, the value is <code>false</code>.</p>"""
    messages: NotRequired[
        "capo_elastic_transcoder.types.exception_messages.ExceptionMessages"
    ]
    """<p>If the <code>Success</code> element contains <code>false</code>, this value is an array of one or more error messages that were generated during the test process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRoleResponse) -> dict:
    out: dict = {}
    if "success" in value:
        out["Success"] = value["success"]
    if "messages" in value:
        import capo_elastic_transcoder.types.exception_messages

        out["Messages"] = (
            capo_elastic_transcoder.types.exception_messages.serialize_json(
                value["messages"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestRoleResponse:
    out: TestRoleResponse = {}  # type: ignore[typeddict-item]
    if "Success" in data:
        out["success"] = data["Success"]
    if "Messages" in data:
        import capo_elastic_transcoder.types.exception_messages

        out["messages"] = (
            capo_elastic_transcoder.types.exception_messages.deserialize_json(
                data["Messages"]
            )
        )
    return out
