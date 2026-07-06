"""Generated from Smithy shape ``com.amazonaws.glue#DeleteConnectionTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class DeleteConnectionTypeRequest(TypedDict, closed=True):
    connection_type: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the connection type to delete. Must reference an existing registered connection type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConnectionTypeRequest) -> dict:
    out: dict = {}
    out["ConnectionType"] = value["connection_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConnectionTypeRequest:
    out: DeleteConnectionTypeRequest = {}  # type: ignore[typeddict-item]
    if "ConnectionType" in data:
        out["connection_type"] = data["ConnectionType"]
    else:
        raise DeserializationError(
            "DeleteConnectionTypeRequest.connection_type required"
        )
    return out
