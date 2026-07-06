"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#PurchaseReservedElasticsearchInstanceOfferingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.guid
    import aws_sdk_elasticsearch_service.types.instance_count
    import aws_sdk_elasticsearch_service.types.reservation_token


class PurchaseReservedElasticsearchInstanceOfferingRequest(TypedDict, closed=True):
    reserved_elasticsearch_instance_offering_id: (
        "aws_sdk_elasticsearch_service.types.guid.GUID"
    )
    """<p>The ID of the reserved Elasticsearch instance offering to purchase.</p>"""
    reservation_name: (
        "aws_sdk_elasticsearch_service.types.reservation_token.ReservationToken"
    )
    """<p>A customer-specified identifier to track this reservation.</p>"""
    instance_count: NotRequired[
        "aws_sdk_elasticsearch_service.types.instance_count.InstanceCount"
    ]
    """<p>The number of Elasticsearch instances to reserve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseReservedElasticsearchInstanceOfferingRequest) -> dict:
    out: dict = {}
    out["ReservedElasticsearchInstanceOfferingId"] = value[
        "reserved_elasticsearch_instance_offering_id"
    ]
    out["ReservationName"] = value["reservation_name"]
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    return out


def deserialize_json(
    data: dict,
) -> PurchaseReservedElasticsearchInstanceOfferingRequest:
    out: PurchaseReservedElasticsearchInstanceOfferingRequest = {}  # type: ignore[typeddict-item]
    if "ReservedElasticsearchInstanceOfferingId" in data:
        out["reserved_elasticsearch_instance_offering_id"] = data[
            "ReservedElasticsearchInstanceOfferingId"
        ]
    else:
        raise DeserializationError(
            "PurchaseReservedElasticsearchInstanceOfferingRequest.reserved_elasticsearch_instance_offering_id required"
        )
    if "ReservationName" in data:
        out["reservation_name"] = data["ReservationName"]
    else:
        raise DeserializationError(
            "PurchaseReservedElasticsearchInstanceOfferingRequest.reservation_name required"
        )
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    return out
