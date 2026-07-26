"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListOfferingsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.offerings
    import capo_device_farm.types.pagination_token


class ListOfferingsResult(TypedDict, closed=True):
    offerings: NotRequired["capo_device_farm.types.offerings.Offerings"]
    """<p>A value that represents the list offering results.</p>"""
    next_token: NotRequired["capo_device_farm.types.pagination_token.PaginationToken"]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfferingsResult) -> dict:
    out: dict = {}
    if "offerings" in value:
        import capo_device_farm.types.offerings

        out["offerings"] = capo_device_farm.types.offerings.serialize_aws_json_1_1(
            value["offerings"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOfferingsResult:
    out: ListOfferingsResult = {}  # type: ignore[typeddict-item]
    if "offerings" in data:
        import capo_device_farm.types.offerings

        out["offerings"] = capo_device_farm.types.offerings.deserialize_aws_json_1_1(
            data["offerings"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
