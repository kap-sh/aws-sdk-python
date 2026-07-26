"""Generated from Smithy shape ``com.amazonaws.networkmanager#StartOrganizationServiceAccessUpdateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.organization_status


class StartOrganizationServiceAccessUpdateResponse(TypedDict, closed=True):
    organization_status: NotRequired[
        "capo_networkmanager.types.organization_status.OrganizationStatus"
    ]
    """<p>The status of the service access update request for an Amazon Web Services Organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartOrganizationServiceAccessUpdateResponse) -> dict:
    out: dict = {}
    if "organization_status" in value:
        import capo_networkmanager.types.organization_status

        out["OrganizationStatus"] = (
            capo_networkmanager.types.organization_status.serialize_json(
                value["organization_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartOrganizationServiceAccessUpdateResponse:
    out: StartOrganizationServiceAccessUpdateResponse = {}  # type: ignore[typeddict-item]
    if "OrganizationStatus" in data:
        import capo_networkmanager.types.organization_status

        out["organization_status"] = (
            capo_networkmanager.types.organization_status.deserialize_json(
                data["OrganizationStatus"]
            )
        )
    return out
