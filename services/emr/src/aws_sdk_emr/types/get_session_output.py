"""Generated from Smithy shape ``com.amazonaws.emr#GetSessionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.session


class GetSessionOutput(TypedDict, closed=True):
    session: NotRequired["aws_sdk_emr.types.session.Session"]
    """<p>The output displays information about the session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSessionOutput) -> dict:
    out: dict = {}
    if "session" in value:
        import aws_sdk_emr.types.session

        out["Session"] = aws_sdk_emr.types.session.serialize_aws_json_1_1(
            value["session"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSessionOutput:
    out: GetSessionOutput = {}  # type: ignore[typeddict-item]
    if "Session" in data:
        import aws_sdk_emr.types.session

        out["session"] = aws_sdk_emr.types.session.deserialize_aws_json_1_1(
            data["Session"]
        )
    return out
