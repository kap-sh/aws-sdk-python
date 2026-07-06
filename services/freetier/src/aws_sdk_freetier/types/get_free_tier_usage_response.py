"""Generated from Smithy shape ``com.amazonaws.freetier#GetFreeTierUsageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_freetier.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_freetier.types.free_tier_usages
    import aws_sdk_freetier.types.next_page_token


class GetFreeTierUsageResponse(TypedDict, closed=True):
    free_tier_usages: "aws_sdk_freetier.types.free_tier_usages.FreeTierUsages"
    """<p>The list of Free Tier usage objects that meet your filter expression.</p>"""
    next_token: NotRequired["aws_sdk_freetier.types.next_page_token.NextPageToken"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetFreeTierUsageResponse) -> dict:
    out: dict = {}
    import aws_sdk_freetier.types.free_tier_usages

    out["freeTierUsages"] = (
        aws_sdk_freetier.types.free_tier_usages.serialize_aws_json_1_0(
            value["free_tier_usages"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetFreeTierUsageResponse:
    out: GetFreeTierUsageResponse = {}  # type: ignore[typeddict-item]
    if "freeTierUsages" in data:
        import aws_sdk_freetier.types.free_tier_usages

        out["free_tier_usages"] = (
            aws_sdk_freetier.types.free_tier_usages.deserialize_aws_json_1_0(
                data["freeTierUsages"]
            )
        )
    else:
        raise DeserializationError("GetFreeTierUsageResponse.free_tier_usages required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
