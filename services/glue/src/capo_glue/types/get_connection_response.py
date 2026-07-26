"""Generated from Smithy shape ``com.amazonaws.glue#GetConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.connection


class GetConnectionResponse(TypedDict, closed=True):
    connection: NotRequired["capo_glue.types.connection.Connection"]
    """<p>The requested connection definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConnectionResponse) -> dict:
    out: dict = {}
    if "connection" in value:
        import capo_glue.types.connection

        out["Connection"] = capo_glue.types.connection.serialize_aws_json_1_1(
            value["connection"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConnectionResponse:
    out: GetConnectionResponse = {}  # type: ignore[typeddict-item]
    if "Connection" in data:
        import capo_glue.types.connection

        out["connection"] = capo_glue.types.connection.deserialize_aws_json_1_1(
            data["Connection"]
        )
    return out
