"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteRecommenderSchemaResponse``."""

from typing_extensions import TypedDict


class DeleteRecommenderSchemaResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecommenderSchemaResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRecommenderSchemaResponse:
    out: DeleteRecommenderSchemaResponse = {}  # type: ignore[typeddict-item]
    return out
