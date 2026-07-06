"""Generated from Smithy shape ``com.amazonaws.schemas#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string


class DeleteResourcePolicyRequest(TypedDict, closed=True):
    registry_name: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The name of the registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
