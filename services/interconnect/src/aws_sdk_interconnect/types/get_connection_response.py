"""Generated from Smithy shape ``com.amazonaws.interconnect#GetConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.connection


class GetConnectionResponse(TypedDict, closed=True):
    connection: NotRequired["aws_sdk_interconnect.types.connection.Connection"]
    """<p>The existing <a>Connection</a> resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetConnectionResponse) -> dict:
    out: dict = {}
    if "connection" in value:
        import aws_sdk_interconnect.types.connection

        out["connection"] = (
            aws_sdk_interconnect.types.connection.serialize_aws_json_1_0(
                value["connection"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetConnectionResponse:
    out: GetConnectionResponse = {}  # type: ignore[typeddict-item]
    if "connection" in data:
        import aws_sdk_interconnect.types.connection

        out["connection"] = (
            aws_sdk_interconnect.types.connection.deserialize_aws_json_1_0(
                data["connection"]
            )
        )
    return out
