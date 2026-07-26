"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#BatchDescribeEntitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_marketplace_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.entity_request_list


class BatchDescribeEntitiesRequest(TypedDict, closed=True):
    entity_request_list: (
        "capo_marketplace_catalog.types.entity_request_list.EntityRequestList"
    )
    """<p>List of entity IDs and the catalogs the entities are present in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDescribeEntitiesRequest) -> dict:
    out: dict = {}
    import capo_marketplace_catalog.types.entity_request_list

    out["EntityRequestList"] = (
        capo_marketplace_catalog.types.entity_request_list.serialize_json(
            value["entity_request_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDescribeEntitiesRequest:
    out: BatchDescribeEntitiesRequest = {}  # type: ignore[typeddict-item]
    if "EntityRequestList" in data:
        import capo_marketplace_catalog.types.entity_request_list

        out["entity_request_list"] = (
            capo_marketplace_catalog.types.entity_request_list.deserialize_json(
                data["EntityRequestList"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDescribeEntitiesRequest.entity_request_list required"
        )
    return out
