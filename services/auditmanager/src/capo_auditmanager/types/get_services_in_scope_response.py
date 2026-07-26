"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetServicesInScopeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.service_metadata_list


class GetServicesInScopeResponse(TypedDict, closed=True):
    service_metadata: NotRequired[
        "capo_auditmanager.types.service_metadata_list.ServiceMetadataList"
    ]
    """<p> The metadata that's associated with the Amazon Web Services service. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServicesInScopeResponse) -> dict:
    out: dict = {}
    if "service_metadata" in value:
        import capo_auditmanager.types.service_metadata_list

        out["serviceMetadata"] = (
            capo_auditmanager.types.service_metadata_list.serialize_json(
                value["service_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetServicesInScopeResponse:
    out: GetServicesInScopeResponse = {}  # type: ignore[typeddict-item]
    if "serviceMetadata" in data:
        import capo_auditmanager.types.service_metadata_list

        out["service_metadata"] = (
            capo_auditmanager.types.service_metadata_list.deserialize_json(
                data["serviceMetadata"]
            )
        )
    return out
