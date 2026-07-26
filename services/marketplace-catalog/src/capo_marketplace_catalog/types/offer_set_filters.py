"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSetFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.offer_set_associated_offer_ids_filter
    import capo_marketplace_catalog.types.offer_set_entity_id_filter
    import capo_marketplace_catalog.types.offer_set_last_modified_date_filter
    import capo_marketplace_catalog.types.offer_set_name_filter
    import capo_marketplace_catalog.types.offer_set_release_date_filter
    import capo_marketplace_catalog.types.offer_set_solution_id_filter
    import capo_marketplace_catalog.types.offer_set_state_filter


class OfferSetFilters(TypedDict, closed=True):
    entity_id: NotRequired[
        "capo_marketplace_catalog.types.offer_set_entity_id_filter.OfferSetEntityIdFilter"
    ]
    """<p>Allows filtering on <code>EntityId</code> of an offer set.</p>"""
    name: NotRequired[
        "capo_marketplace_catalog.types.offer_set_name_filter.OfferSetNameFilter"
    ]
    """<p>Allows filtering on the <code>Name</code> of an offer set.</p>"""
    state: NotRequired[
        "capo_marketplace_catalog.types.offer_set_state_filter.OfferSetStateFilter"
    ]
    """<p>Allows filtering on the <code>State</code> of an offer set.</p>"""
    release_date: NotRequired[
        "capo_marketplace_catalog.types.offer_set_release_date_filter.OfferSetReleaseDateFilter"
    ]
    """<p>Allows filtering on the <code>ReleaseDate</code> of an offer set.</p>"""
    associated_offer_ids: NotRequired[
        "capo_marketplace_catalog.types.offer_set_associated_offer_ids_filter.OfferSetAssociatedOfferIdsFilter"
    ]
    """<p>Allows filtering on the <code>AssociatedOfferIds</code> of an offer set.</p>"""
    solution_id: NotRequired[
        "capo_marketplace_catalog.types.offer_set_solution_id_filter.OfferSetSolutionIdFilter"
    ]
    """<p>Allows filtering on the <code>SolutionId</code> of an offer set.</p>"""
    last_modified_date: NotRequired[
        "capo_marketplace_catalog.types.offer_set_last_modified_date_filter.OfferSetLastModifiedDateFilter"
    ]
    """<p>Allows filtering on the <code>LastModifiedDate</code> of an offer set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetFilters) -> dict:
    out: dict = {}
    if "entity_id" in value:
        import capo_marketplace_catalog.types.offer_set_entity_id_filter

        out["EntityId"] = (
            capo_marketplace_catalog.types.offer_set_entity_id_filter.serialize_json(
                value["entity_id"]
            )
        )
    if "name" in value:
        import capo_marketplace_catalog.types.offer_set_name_filter

        out["Name"] = (
            capo_marketplace_catalog.types.offer_set_name_filter.serialize_json(
                value["name"]
            )
        )
    if "state" in value:
        import capo_marketplace_catalog.types.offer_set_state_filter

        out["State"] = (
            capo_marketplace_catalog.types.offer_set_state_filter.serialize_json(
                value["state"]
            )
        )
    if "release_date" in value:
        import capo_marketplace_catalog.types.offer_set_release_date_filter

        out["ReleaseDate"] = (
            capo_marketplace_catalog.types.offer_set_release_date_filter.serialize_json(
                value["release_date"]
            )
        )
    if "associated_offer_ids" in value:
        import capo_marketplace_catalog.types.offer_set_associated_offer_ids_filter

        out["AssociatedOfferIds"] = (
            capo_marketplace_catalog.types.offer_set_associated_offer_ids_filter.serialize_json(
                value["associated_offer_ids"]
            )
        )
    if "solution_id" in value:
        import capo_marketplace_catalog.types.offer_set_solution_id_filter

        out["SolutionId"] = (
            capo_marketplace_catalog.types.offer_set_solution_id_filter.serialize_json(
                value["solution_id"]
            )
        )
    if "last_modified_date" in value:
        import capo_marketplace_catalog.types.offer_set_last_modified_date_filter

        out["LastModifiedDate"] = (
            capo_marketplace_catalog.types.offer_set_last_modified_date_filter.serialize_json(
                value["last_modified_date"]
            )
        )
    return out


def deserialize_json(data: dict) -> OfferSetFilters:
    out: OfferSetFilters = {}  # type: ignore[typeddict-item]
    if "EntityId" in data:
        import capo_marketplace_catalog.types.offer_set_entity_id_filter

        out["entity_id"] = (
            capo_marketplace_catalog.types.offer_set_entity_id_filter.deserialize_json(
                data["EntityId"]
            )
        )
    if "Name" in data:
        import capo_marketplace_catalog.types.offer_set_name_filter

        out["name"] = (
            capo_marketplace_catalog.types.offer_set_name_filter.deserialize_json(
                data["Name"]
            )
        )
    if "State" in data:
        import capo_marketplace_catalog.types.offer_set_state_filter

        out["state"] = (
            capo_marketplace_catalog.types.offer_set_state_filter.deserialize_json(
                data["State"]
            )
        )
    if "ReleaseDate" in data:
        import capo_marketplace_catalog.types.offer_set_release_date_filter

        out["release_date"] = (
            capo_marketplace_catalog.types.offer_set_release_date_filter.deserialize_json(
                data["ReleaseDate"]
            )
        )
    if "AssociatedOfferIds" in data:
        import capo_marketplace_catalog.types.offer_set_associated_offer_ids_filter

        out["associated_offer_ids"] = (
            capo_marketplace_catalog.types.offer_set_associated_offer_ids_filter.deserialize_json(
                data["AssociatedOfferIds"]
            )
        )
    if "SolutionId" in data:
        import capo_marketplace_catalog.types.offer_set_solution_id_filter

        out["solution_id"] = (
            capo_marketplace_catalog.types.offer_set_solution_id_filter.deserialize_json(
                data["SolutionId"]
            )
        )
    if "LastModifiedDate" in data:
        import capo_marketplace_catalog.types.offer_set_last_modified_date_filter

        out["last_modified_date"] = (
            capo_marketplace_catalog.types.offer_set_last_modified_date_filter.deserialize_json(
                data["LastModifiedDate"]
            )
        )
    return out
