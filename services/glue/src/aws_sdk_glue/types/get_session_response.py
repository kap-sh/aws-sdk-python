"""Generated from Smithy shape ``com.amazonaws.glue#GetSessionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.session


class GetSessionResponse(TypedDict):
    session: NotRequired["aws_sdk_glue.types.session.Session"]
    """<p>The session object is returned in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSessionResponse) -> dict:
    out: dict = {}
    if "session" in value:
        import aws_sdk_glue.types.session

        out["Session"] = aws_sdk_glue.types.session.serialize_aws_json_1_1(
            value["session"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSessionResponse:
    out: GetSessionResponse = {}  # type: ignore[typeddict-item]
    if "Session" in data:
        import aws_sdk_glue.types.session

        out["session"] = aws_sdk_glue.types.session.deserialize_aws_json_1_1(
            data["Session"]
        )
    return out
