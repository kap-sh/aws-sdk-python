"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#BatchDescribeEntitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.entity_details
    import capo_marketplace_catalog.types.errors


class BatchDescribeEntitiesResponse(TypedDict, closed=True):
    entity_details: NotRequired[
        "capo_marketplace_catalog.types.entity_details.EntityDetails"
    ]
    """<p>Details about each entity.</p>"""
    errors: NotRequired["capo_marketplace_catalog.types.errors.Errors"]
    """<p>A map of errors returned, with <code>EntityId</code> as the key and <code>errorDetail</code> as the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDescribeEntitiesResponse) -> dict:
    out: dict = {}
    if "entity_details" in value:
        import capo_marketplace_catalog.types.entity_details

        out["EntityDetails"] = (
            capo_marketplace_catalog.types.entity_details.serialize_json(
                value["entity_details"]
            )
        )
    if "errors" in value:
        import capo_marketplace_catalog.types.errors

        out["Errors"] = capo_marketplace_catalog.types.errors.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> BatchDescribeEntitiesResponse:
    out: BatchDescribeEntitiesResponse = {}  # type: ignore[typeddict-item]
    if "EntityDetails" in data:
        import capo_marketplace_catalog.types.entity_details

        out["entity_details"] = (
            capo_marketplace_catalog.types.entity_details.deserialize_json(
                data["EntityDetails"]
            )
        )
    if "Errors" in data:
        import capo_marketplace_catalog.types.errors

        out["errors"] = capo_marketplace_catalog.types.errors.deserialize_json(
            data["Errors"]
        )
    return out
