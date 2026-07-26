"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#DeleteSuiteDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.uuid


class DeleteSuiteDefinitionRequest(TypedDict, closed=True):
    suite_definition_id: "capo_iotdeviceadvisor.types.uuid.UUID"
    """<p>Suite definition ID of the test suite to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSuiteDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSuiteDefinitionRequest:
    out: DeleteSuiteDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
