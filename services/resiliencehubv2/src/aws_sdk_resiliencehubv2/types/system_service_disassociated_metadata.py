"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemServiceDisassociatedMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.user_journey_name_list


class SystemServiceDisassociatedMetadata(TypedDict):
    service_name: NotRequired["str"]
    """<p>The name of the disassociated service.</p>"""
    service_arn: NotRequired["aws_sdk_resiliencehubv2.types.arn.Arn"]
    user_journeys_affected: NotRequired[
        "aws_sdk_resiliencehubv2.types.user_journey_name_list.UserJourneyNameList"
    ]
    """<p>The user journeys affected by the disassociation.</p>"""
    comment: NotRequired["str"]
    """<p>A comment about the disassociation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemServiceDisassociatedMetadata) -> dict:
    out: dict = {}
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "user_journeys_affected" in value:
        import aws_sdk_resiliencehubv2.types.user_journey_name_list

        out["userJourneysAffected"] = (
            aws_sdk_resiliencehubv2.types.user_journey_name_list.serialize_json(
                value["user_journeys_affected"]
            )
        )
    if "comment" in value:
        out["comment"] = value["comment"]
    return out


def deserialize_json(data: dict) -> SystemServiceDisassociatedMetadata:
    out: SystemServiceDisassociatedMetadata = {}  # type: ignore[typeddict-item]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    if "userJourneysAffected" in data:
        import aws_sdk_resiliencehubv2.types.user_journey_name_list

        out["user_journeys_affected"] = (
            aws_sdk_resiliencehubv2.types.user_journey_name_list.deserialize_json(
                data["userJourneysAffected"]
            )
        )
    if "comment" in data:
        out["comment"] = data["comment"]
    return out
