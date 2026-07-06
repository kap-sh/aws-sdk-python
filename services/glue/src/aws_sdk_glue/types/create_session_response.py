"""Generated from Smithy shape ``com.amazonaws.glue#CreateSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.session


class CreateSessionResponse(TypedDict, closed=True):
    session: NotRequired["aws_sdk_glue.types.session.Session"]
    """<p>Returns the session object in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSessionResponse) -> dict:
    out: dict = {}
    if "session" in value:
        import aws_sdk_glue.types.session

        out["Session"] = aws_sdk_glue.types.session.serialize_aws_json_1_1(
            value["session"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSessionResponse:
    out: CreateSessionResponse = {}  # type: ignore[typeddict-item]
    if "Session" in data:
        import aws_sdk_glue.types.session

        out["session"] = aws_sdk_glue.types.session.deserialize_aws_json_1_1(
            data["Session"]
        )
    return out
