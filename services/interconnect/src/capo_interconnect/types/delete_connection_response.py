"""Generated from Smithy shape ``com.amazonaws.interconnect#DeleteConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_interconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_interconnect.types.connection


class DeleteConnectionResponse(TypedDict, closed=True):
    connection: "capo_interconnect.types.connection.Connection"
    """<p>The <a>Connection</a> object that has been marked for deletion.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteConnectionResponse) -> dict:
    out: dict = {}
    import capo_interconnect.types.connection

    out["connection"] = capo_interconnect.types.connection.serialize_aws_json_1_0(
        value["connection"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteConnectionResponse:
    out: DeleteConnectionResponse = {}  # type: ignore[typeddict-item]
    if "connection" in data:
        import capo_interconnect.types.connection

        out["connection"] = capo_interconnect.types.connection.deserialize_aws_json_1_0(
            data["connection"]
        )
    else:
        raise DeserializationError("DeleteConnectionResponse.connection required")
    return out
