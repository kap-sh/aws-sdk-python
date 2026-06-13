"""Generated from Smithy shape ``com.amazonaws.omics#GetRunGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.run_group_id


class GetRunGroupRequest(TypedDict):
    id: "aws_sdk_omics.types.run_group_id.RunGroupId"
    """<p>The group's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRunGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRunGroupRequest:
    out: GetRunGroupRequest = {}  # type: ignore[typeddict-item]
    return out
