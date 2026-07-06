"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#PurchaseReservedElasticsearchInstanceOfferingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.guid
    import aws_sdk_elasticsearch_service.types.reservation_token


class PurchaseReservedElasticsearchInstanceOfferingResponse(TypedDict, closed=True):
    reserved_elasticsearch_instance_id: NotRequired[
        "aws_sdk_elasticsearch_service.types.guid.GUID"
    ]
    """<p>Details of the reserved Elasticsearch instance which was purchased.</p>"""
    reservation_name: NotRequired[
        "aws_sdk_elasticsearch_service.types.reservation_token.ReservationToken"
    ]
    """<p>The customer-specified identifier used to track this reservation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: PurchaseReservedElasticsearchInstanceOfferingResponse,
) -> dict:
    out: dict = {}
    if "reserved_elasticsearch_instance_id" in value:
        out["ReservedElasticsearchInstanceId"] = value[
            "reserved_elasticsearch_instance_id"
        ]
    if "reservation_name" in value:
        out["ReservationName"] = value["reservation_name"]
    return out


def deserialize_json(
    data: dict,
) -> PurchaseReservedElasticsearchInstanceOfferingResponse:
    out: PurchaseReservedElasticsearchInstanceOfferingResponse = {}  # type: ignore[typeddict-item]
    if "ReservedElasticsearchInstanceId" in data:
        out["reserved_elasticsearch_instance_id"] = data[
            "ReservedElasticsearchInstanceId"
        ]
    if "ReservationName" in data:
        out["reservation_name"] = data["ReservationName"]
    return out
