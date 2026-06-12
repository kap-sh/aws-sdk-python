"""Generated from Smithy shape ``com.amazonaws.dataexchange#DeleteDataSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.id


class DeleteDataSetRequest(TypedDict):
    data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for a data set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataSetRequest:
    out: DeleteDataSetRequest = {}  # type: ignore[typeddict-item]
    return out
