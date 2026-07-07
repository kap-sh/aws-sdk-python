"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.date_time_iso8601
    import aws_sdk_marketplace_catalog.types.offer_set_associated_offer_ids_list
    import aws_sdk_marketplace_catalog.types.offer_set_name_string
    import aws_sdk_marketplace_catalog.types.offer_set_solution_id_string
    import aws_sdk_marketplace_catalog.types.offer_set_state_string


class OfferSetSummary(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_set_name_string.OfferSetNameString"
    ]
    """<p>The name of the offer set.</p>"""
    state: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_set_state_string.OfferSetStateString"
    ]
    """<p>The state of the offer set.</p>"""
    release_date: NotRequired[
        "aws_sdk_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The release date of the offer set.</p>"""
    associated_offer_ids: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_set_associated_offer_ids_list.OfferSetAssociatedOfferIdsList"
    ]
    """<p>The list of offer IDs associated with the offer set.</p>"""
    solution_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_set_solution_id_string.OfferSetSolutionIdString"
    ]
    """<p>The solution ID associated with the offer set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "state" in value:
        import aws_sdk_marketplace_catalog.types.offer_set_state_string

        out["State"] = (
            aws_sdk_marketplace_catalog.types.offer_set_state_string.serialize_json(
                value["state"]
            )
        )
    if "release_date" in value:
        out["ReleaseDate"] = value["release_date"]
    if "associated_offer_ids" in value:
        import aws_sdk_marketplace_catalog.types.offer_set_associated_offer_ids_list

        out["AssociatedOfferIds"] = (
            aws_sdk_marketplace_catalog.types.offer_set_associated_offer_ids_list.serialize_json(
                value["associated_offer_ids"]
            )
        )
    if "solution_id" in value:
        out["SolutionId"] = value["solution_id"]
    return out


def deserialize_json(data: dict) -> OfferSetSummary:
    out: OfferSetSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "State" in data:
        import aws_sdk_marketplace_catalog.types.offer_set_state_string

        out["state"] = (
            aws_sdk_marketplace_catalog.types.offer_set_state_string.deserialize_json(
                data["State"]
            )
        )
    if "ReleaseDate" in data:
        out["release_date"] = data["ReleaseDate"]
    if "AssociatedOfferIds" in data:
        import aws_sdk_marketplace_catalog.types.offer_set_associated_offer_ids_list

        out["associated_offer_ids"] = (
            aws_sdk_marketplace_catalog.types.offer_set_associated_offer_ids_list.deserialize_json(
                data["AssociatedOfferIds"]
            )
        )
    if "SolutionId" in data:
        out["solution_id"] = data["SolutionId"]
    return out
