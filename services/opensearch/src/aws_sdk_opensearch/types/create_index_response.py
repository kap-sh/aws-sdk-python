"""Generated from Smithy shape ``com.amazonaws.opensearch#CreateIndexResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.index_status


class CreateIndexResponse(TypedDict):
    status: "aws_sdk_opensearch.types.index_status.IndexStatus"
    """<p>The status of the index creation operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIndexResponse) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.index_status

    out["Status"] = aws_sdk_opensearch.types.index_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> CreateIndexResponse:
    out: CreateIndexResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_opensearch.types.index_status

        out["status"] = aws_sdk_opensearch.types.index_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("CreateIndexResponse.status required")
    return out
