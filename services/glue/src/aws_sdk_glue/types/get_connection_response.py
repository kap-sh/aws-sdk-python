"""Generated from Smithy shape ``com.amazonaws.glue#GetConnectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.connection


class GetConnectionResponse(TypedDict):
    connection: NotRequired["aws_sdk_glue.types.connection.Connection"]
    """<p>The requested connection definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConnectionResponse) -> dict:
    out: dict = {}
    if "connection" in value:
        import aws_sdk_glue.types.connection

        out["Connection"] = aws_sdk_glue.types.connection.serialize_aws_json_1_1(
            value["connection"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConnectionResponse:
    out: GetConnectionResponse = {}  # type: ignore[typeddict-item]
    if "Connection" in data:
        import aws_sdk_glue.types.connection

        out["connection"] = aws_sdk_glue.types.connection.deserialize_aws_json_1_1(
            data["Connection"]
        )
    return out
