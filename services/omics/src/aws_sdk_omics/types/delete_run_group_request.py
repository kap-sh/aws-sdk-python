"""Generated from Smithy shape ``com.amazonaws.omics#DeleteRunGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.run_group_id


class DeleteRunGroupRequest(TypedDict):
    id: "aws_sdk_omics.types.run_group_id.RunGroupId"
    """<p>The run group's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRunGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRunGroupRequest:
    out: DeleteRunGroupRequest = {}  # type: ignore[typeddict-item]
    return out
