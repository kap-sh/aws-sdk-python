"""Generated from Smithy shape ``com.amazonaws.finspacedata#GetChangesetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.changeset_id
    import aws_sdk_finspace_data.types.dataset_id


class GetChangesetRequest(TypedDict, closed=True):
    dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId"
    """<p>The unique identifier for the FinSpace Dataset where the Changeset is created.</p>"""
    changeset_id: "aws_sdk_finspace_data.types.changeset_id.ChangesetId"
    """<p>The unique identifier of the Changeset for which to get data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChangesetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetChangesetRequest:
    out: GetChangesetRequest = {}  # type: ignore[typeddict-item]
    return out
