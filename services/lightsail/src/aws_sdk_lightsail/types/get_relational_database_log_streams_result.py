"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseLogStreamsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.string_list


class GetRelationalDatabaseLogStreamsResult(TypedDict, closed=True):
    log_streams: NotRequired["aws_sdk_lightsail.types.string_list.StringList"]
    """<p>An object describing the result of your get relational database log streams request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabaseLogStreamsResult) -> dict:
    out: dict = {}
    if "log_streams" in value:
        import aws_sdk_lightsail.types.string_list

        out["logStreams"] = aws_sdk_lightsail.types.string_list.serialize_aws_json_1_1(
            value["log_streams"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabaseLogStreamsResult:
    out: GetRelationalDatabaseLogStreamsResult = {}  # type: ignore[typeddict-item]
    if "logStreams" in data:
        import aws_sdk_lightsail.types.string_list

        out["log_streams"] = (
            aws_sdk_lightsail.types.string_list.deserialize_aws_json_1_1(
                data["logStreams"]
            )
        )
    return out
