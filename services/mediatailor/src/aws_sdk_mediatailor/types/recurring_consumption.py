"""Generated from Smithy shape ``com.amazonaws.mediatailor#RecurringConsumption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__integer
    import aws_sdk_mediatailor.types.__list_of_avail_matching_criteria


class RecurringConsumption(TypedDict):
    retrieved_ad_expiration_seconds: NotRequired[
        "aws_sdk_mediatailor.types.__integer.__integer"
    ]
    """<p>The number of seconds that an ad is available for insertion after it was prefetched.</p>"""
    avail_matching_criteria: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_avail_matching_criteria.__listOfAvailMatchingCriteria"
    ]
    """<p>The configuration for the dynamic variables that determine which ad breaks that MediaTailor inserts prefetched ads in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecurringConsumption) -> dict:
    out: dict = {}
    if "retrieved_ad_expiration_seconds" in value:
        out["RetrievedAdExpirationSeconds"] = value["retrieved_ad_expiration_seconds"]
    if "avail_matching_criteria" in value:
        import aws_sdk_mediatailor.types.__list_of_avail_matching_criteria

        out["AvailMatchingCriteria"] = (
            aws_sdk_mediatailor.types.__list_of_avail_matching_criteria.serialize_json(
                value["avail_matching_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecurringConsumption:
    out: RecurringConsumption = {}  # type: ignore[typeddict-item]
    if "RetrievedAdExpirationSeconds" in data:
        out["retrieved_ad_expiration_seconds"] = data["RetrievedAdExpirationSeconds"]
    if "AvailMatchingCriteria" in data:
        import aws_sdk_mediatailor.types.__list_of_avail_matching_criteria

        out["avail_matching_criteria"] = (
            aws_sdk_mediatailor.types.__list_of_avail_matching_criteria.deserialize_json(
                data["AvailMatchingCriteria"]
            )
        )
    return out
