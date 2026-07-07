"""Generated from Smithy shape ``com.amazonaws.codestarconnections#GetConnectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.connection


class GetConnectionOutput(TypedDict, closed=True):
    connection: NotRequired["aws_sdk_codestar_connections.types.connection.Connection"]
    """<p>The connection details, such as status, owner, and provider type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetConnectionOutput) -> dict:
    out: dict = {}
    if "connection" in value:
        import aws_sdk_codestar_connections.types.connection

        out["Connection"] = (
            aws_sdk_codestar_connections.types.connection.serialize_aws_json_1_0(
                value["connection"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetConnectionOutput:
    out: GetConnectionOutput = {}  # type: ignore[typeddict-item]
    if "Connection" in data:
        import aws_sdk_codestar_connections.types.connection

        out["connection"] = (
            aws_sdk_codestar_connections.types.connection.deserialize_aws_json_1_0(
                data["Connection"]
            )
        )
    return out
