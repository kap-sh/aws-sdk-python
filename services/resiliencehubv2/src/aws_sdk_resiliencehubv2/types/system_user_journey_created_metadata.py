"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemUserJourneyCreatedMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.service_reference_list


class SystemUserJourneyCreatedMetadata(TypedDict, closed=True):
    user_journey_name: NotRequired["str"]
    """<p>The name of the created user journey.</p>"""
    associated_services: NotRequired[
        "aws_sdk_resiliencehubv2.types.service_reference_list.ServiceReferenceList"
    ]
    """<p>The services associated with the created user journey.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemUserJourneyCreatedMetadata) -> dict:
    out: dict = {}
    if "user_journey_name" in value:
        out["userJourneyName"] = value["user_journey_name"]
    if "associated_services" in value:
        import aws_sdk_resiliencehubv2.types.service_reference_list

        out["associatedServices"] = (
            aws_sdk_resiliencehubv2.types.service_reference_list.serialize_json(
                value["associated_services"]
            )
        )
    return out


def deserialize_json(data: dict) -> SystemUserJourneyCreatedMetadata:
    out: SystemUserJourneyCreatedMetadata = {}  # type: ignore[typeddict-item]
    if "userJourneyName" in data:
        out["user_journey_name"] = data["userJourneyName"]
    if "associatedServices" in data:
        import aws_sdk_resiliencehubv2.types.service_reference_list

        out["associated_services"] = (
            aws_sdk_resiliencehubv2.types.service_reference_list.deserialize_json(
                data["associatedServices"]
            )
        )
    return out
