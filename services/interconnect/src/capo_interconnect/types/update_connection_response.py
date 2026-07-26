"""Generated from Smithy shape ``com.amazonaws.interconnect#UpdateConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.connection


class UpdateConnectionResponse(TypedDict, closed=True):
    connection: NotRequired["capo_interconnect.types.connection.Connection"]
    """<p>The resulting updated <a>Connection</a> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateConnectionResponse) -> dict:
    out: dict = {}
    if "connection" in value:
        import capo_interconnect.types.connection

        out["connection"] = capo_interconnect.types.connection.serialize_aws_json_1_0(
            value["connection"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateConnectionResponse:
    out: UpdateConnectionResponse = {}  # type: ignore[typeddict-item]
    if "connection" in data:
        import capo_interconnect.types.connection

        out["connection"] = capo_interconnect.types.connection.deserialize_aws_json_1_0(
            data["connection"]
        )
    return out
