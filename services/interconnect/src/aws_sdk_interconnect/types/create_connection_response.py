"""Generated from Smithy shape ``com.amazonaws.interconnect#CreateConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.connection


class CreateConnectionResponse(TypedDict, closed=True):
    connection: NotRequired["aws_sdk_interconnect.types.connection.Connection"]
    """<p>The resulting <a>Connection</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateConnectionResponse) -> dict:
    out: dict = {}
    if "connection" in value:
        import aws_sdk_interconnect.types.connection

        out["connection"] = (
            aws_sdk_interconnect.types.connection.serialize_aws_json_1_0(
                value["connection"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateConnectionResponse:
    out: CreateConnectionResponse = {}  # type: ignore[typeddict-item]
    if "connection" in data:
        import aws_sdk_interconnect.types.connection

        out["connection"] = (
            aws_sdk_interconnect.types.connection.deserialize_aws_json_1_0(
                data["connection"]
            )
        )
    return out
