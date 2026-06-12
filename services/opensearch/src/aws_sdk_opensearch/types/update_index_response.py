"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateIndexResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.index_status


class UpdateIndexResponse(TypedDict):
    status: "aws_sdk_opensearch.types.index_status.IndexStatus"
    """<p>The status of the index update operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIndexResponse) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.index_status

    out["Status"] = aws_sdk_opensearch.types.index_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateIndexResponse:
    out: UpdateIndexResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_opensearch.types.index_status

        out["status"] = aws_sdk_opensearch.types.index_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("UpdateIndexResponse.status required")
    return out
