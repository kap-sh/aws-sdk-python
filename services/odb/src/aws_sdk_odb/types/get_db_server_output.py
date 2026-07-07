"""Generated from Smithy shape ``com.amazonaws.odb#GetDbServerOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.db_server


class GetDbServerOutput(TypedDict, closed=True):
    db_server: NotRequired["aws_sdk_odb.types.db_server.DbServer"]
    """<p>The details of the requested database server.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDbServerOutput) -> dict:
    out: dict = {}
    if "db_server" in value:
        import aws_sdk_odb.types.db_server

        out["dbServer"] = aws_sdk_odb.types.db_server.serialize_aws_json_1_0(
            value["db_server"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDbServerOutput:
    out: GetDbServerOutput = {}  # type: ignore[typeddict-item]
    if "dbServer" in data:
        import aws_sdk_odb.types.db_server

        out["db_server"] = aws_sdk_odb.types.db_server.deserialize_aws_json_1_0(
            data["dbServer"]
        )
    return out
