"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UserJourneyChanges``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.service_reference_changes
    import aws_sdk_resiliencehubv2.types.string_change


class UserJourneyChanges(TypedDict):
    journey_description: NotRequired[
        "aws_sdk_resiliencehubv2.types.string_change.StringChange"
    ]
    """<p>Changes to the user journey description.</p>"""
    associated_services: NotRequired[
        "aws_sdk_resiliencehubv2.types.service_reference_changes.ServiceReferenceChanges"
    ]
    """<p>Changes to the services associated with the user journey.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserJourneyChanges) -> dict:
    out: dict = {}
    if "journey_description" in value:
        import aws_sdk_resiliencehubv2.types.string_change

        out["journeyDescription"] = (
            aws_sdk_resiliencehubv2.types.string_change.serialize_json(
                value["journey_description"]
            )
        )
    if "associated_services" in value:
        import aws_sdk_resiliencehubv2.types.service_reference_changes

        out["associatedServices"] = (
            aws_sdk_resiliencehubv2.types.service_reference_changes.serialize_json(
                value["associated_services"]
            )
        )
    return out


def deserialize_json(data: dict) -> UserJourneyChanges:
    out: UserJourneyChanges = {}  # type: ignore[typeddict-item]
    if "journeyDescription" in data:
        import aws_sdk_resiliencehubv2.types.string_change

        out["journey_description"] = (
            aws_sdk_resiliencehubv2.types.string_change.deserialize_json(
                data["journeyDescription"]
            )
        )
    if "associatedServices" in data:
        import aws_sdk_resiliencehubv2.types.service_reference_changes

        out["associated_services"] = (
            aws_sdk_resiliencehubv2.types.service_reference_changes.deserialize_json(
                data["associatedServices"]
            )
        )
    return out
