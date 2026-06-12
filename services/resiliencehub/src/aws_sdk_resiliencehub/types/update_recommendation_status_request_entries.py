"""Generated from Smithy shape ``com.amazonaws.resiliencehub#UpdateRecommendationStatusRequestEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.update_recommendation_status_request_entry

UpdateRecommendationStatusRequestEntries: TypeAlias = list[
    "aws_sdk_resiliencehub.types.update_recommendation_status_request_entry.UpdateRecommendationStatusRequestEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommendationStatusRequestEntries) -> list:
    import aws_sdk_resiliencehub.types.update_recommendation_status_request_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehub.types.update_recommendation_status_request_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UpdateRecommendationStatusRequestEntries:
    import aws_sdk_resiliencehub.types.update_recommendation_status_request_entry

    out: UpdateRecommendationStatusRequestEntries = []
    for item in data:
        out.append(
            aws_sdk_resiliencehub.types.update_recommendation_status_request_entry.deserialize_json(
                item
            )
        )
    return out
