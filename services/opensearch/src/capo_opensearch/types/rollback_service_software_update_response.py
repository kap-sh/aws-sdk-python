"""Generated from Smithy shape ``com.amazonaws.opensearch#RollbackServiceSoftwareUpdateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.rollback_service_software_options


class RollbackServiceSoftwareUpdateResponse(TypedDict, closed=True):
    rollback_service_software_options: NotRequired[
        "capo_opensearch.types.rollback_service_software_options.RollbackServiceSoftwareOptions"
    ]
    """<p>The rollback options for the service software update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RollbackServiceSoftwareUpdateResponse) -> dict:
    out: dict = {}
    if "rollback_service_software_options" in value:
        import capo_opensearch.types.rollback_service_software_options

        out["RollbackServiceSoftwareOptions"] = (
            capo_opensearch.types.rollback_service_software_options.serialize_json(
                value["rollback_service_software_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> RollbackServiceSoftwareUpdateResponse:
    out: RollbackServiceSoftwareUpdateResponse = {}  # type: ignore[typeddict-item]
    if "RollbackServiceSoftwareOptions" in data:
        import capo_opensearch.types.rollback_service_software_options

        out["rollback_service_software_options"] = (
            capo_opensearch.types.rollback_service_software_options.deserialize_json(
                data["RollbackServiceSoftwareOptions"]
            )
        )
    return out
