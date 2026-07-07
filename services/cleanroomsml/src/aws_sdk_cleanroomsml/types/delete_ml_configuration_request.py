"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DeleteMLConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.uuid


class DeleteMLConfigurationRequest(TypedDict, closed=True):
    membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the of the member that is deleting the ML modeling configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMLConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMLConfigurationRequest:
    out: DeleteMLConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
