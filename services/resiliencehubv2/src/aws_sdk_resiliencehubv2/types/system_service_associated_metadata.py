"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemServiceAssociatedMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.user_journey_name_list


class SystemServiceAssociatedMetadata(TypedDict):
    service_name: NotRequired["str"]
    """<p>The name of the associated service.</p>"""
    service_arn: NotRequired["aws_sdk_resiliencehubv2.types.arn.Arn"]
    user_journeys: NotRequired[
        "aws_sdk_resiliencehubv2.types.user_journey_name_list.UserJourneyNameList"
    ]
    """<p>The user journeys linking the service to the system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemServiceAssociatedMetadata) -> dict:
    out: dict = {}
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "user_journeys" in value:
        import aws_sdk_resiliencehubv2.types.user_journey_name_list

        out["userJourneys"] = (
            aws_sdk_resiliencehubv2.types.user_journey_name_list.serialize_json(
                value["user_journeys"]
            )
        )
    return out


def deserialize_json(data: dict) -> SystemServiceAssociatedMetadata:
    out: SystemServiceAssociatedMetadata = {}  # type: ignore[typeddict-item]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    if "userJourneys" in data:
        import aws_sdk_resiliencehubv2.types.user_journey_name_list

        out["user_journeys"] = (
            aws_sdk_resiliencehubv2.types.user_journey_name_list.deserialize_json(
                data["userJourneys"]
            )
        )
    return out
