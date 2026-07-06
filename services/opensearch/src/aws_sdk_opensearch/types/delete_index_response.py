"""Generated from Smithy shape ``com.amazonaws.opensearch#DeleteIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.index_status


class DeleteIndexResponse(TypedDict, closed=True):
    status: "aws_sdk_opensearch.types.index_status.IndexStatus"
    """<p>The status of the index deletion operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIndexResponse) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.index_status

    out["Status"] = aws_sdk_opensearch.types.index_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteIndexResponse:
    out: DeleteIndexResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_opensearch.types.index_status

        out["status"] = aws_sdk_opensearch.types.index_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("DeleteIndexResponse.status required")
    return out
