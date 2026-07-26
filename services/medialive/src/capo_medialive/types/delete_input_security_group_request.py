"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteInputSecurityGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class DeleteInputSecurityGroupRequest(TypedDict, closed=True):
    input_security_group_id: "capo_medialive.types.__string.__string"
    """The Input Security Group to delete"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInputSecurityGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteInputSecurityGroupRequest:
    out: DeleteInputSecurityGroupRequest = {}  # type: ignore[typeddict-item]
    return out
