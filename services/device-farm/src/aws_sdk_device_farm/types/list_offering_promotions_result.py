"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListOfferingPromotionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.offering_promotions
    import aws_sdk_device_farm.types.pagination_token


class ListOfferingPromotionsResult(TypedDict):
    offering_promotions: NotRequired[
        "aws_sdk_device_farm.types.offering_promotions.OfferingPromotions"
    ]
    """<p>Information about the offering promotions.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>An identifier to be used in the next call to this operation, to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfferingPromotionsResult) -> dict:
    out: dict = {}
    if "offering_promotions" in value:
        import aws_sdk_device_farm.types.offering_promotions

        out["offeringPromotions"] = (
            aws_sdk_device_farm.types.offering_promotions.serialize_aws_json_1_1(
                value["offering_promotions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOfferingPromotionsResult:
    out: ListOfferingPromotionsResult = {}  # type: ignore[typeddict-item]
    if "offeringPromotions" in data:
        import aws_sdk_device_farm.types.offering_promotions

        out["offering_promotions"] = (
            aws_sdk_device_farm.types.offering_promotions.deserialize_aws_json_1_1(
                data["offeringPromotions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
