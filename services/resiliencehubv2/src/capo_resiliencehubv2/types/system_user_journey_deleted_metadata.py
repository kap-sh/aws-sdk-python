"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemUserJourneyDeletedMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.service_reference_list


class SystemUserJourneyDeletedMetadata(TypedDict, closed=True):
    user_journey_name: NotRequired["str"]
    """<p>The name of the deleted user journey.</p>"""
    associated_services_at_deletion: NotRequired[
        "capo_resiliencehubv2.types.service_reference_list.ServiceReferenceList"
    ]
    """<p>The services that were associated at the time of deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemUserJourneyDeletedMetadata) -> dict:
    out: dict = {}
    if "user_journey_name" in value:
        out["userJourneyName"] = value["user_journey_name"]
    if "associated_services_at_deletion" in value:
        import capo_resiliencehubv2.types.service_reference_list

        out["associatedServicesAtDeletion"] = (
            capo_resiliencehubv2.types.service_reference_list.serialize_json(
                value["associated_services_at_deletion"]
            )
        )
    return out


def deserialize_json(data: dict) -> SystemUserJourneyDeletedMetadata:
    out: SystemUserJourneyDeletedMetadata = {}  # type: ignore[typeddict-item]
    if "userJourneyName" in data:
        out["user_journey_name"] = data["userJourneyName"]
    if "associatedServicesAtDeletion" in data:
        import capo_resiliencehubv2.types.service_reference_list

        out["associated_services_at_deletion"] = (
            capo_resiliencehubv2.types.service_reference_list.deserialize_json(
                data["associatedServicesAtDeletion"]
            )
        )
    return out
