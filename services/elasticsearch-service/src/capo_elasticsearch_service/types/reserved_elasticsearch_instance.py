"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ReservedElasticsearchInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.double
    import capo_elasticsearch_service.types.es_partition_instance_type
    import capo_elasticsearch_service.types.guid
    import capo_elasticsearch_service.types.integer
    import capo_elasticsearch_service.types.recurring_charge_list
    import capo_elasticsearch_service.types.reservation_token
    import capo_elasticsearch_service.types.reserved_elasticsearch_instance_payment_option
    import capo_elasticsearch_service.types.string
    import capo_elasticsearch_service.types.update_timestamp


class ReservedElasticsearchInstance(TypedDict, closed=True):
    reservation_name: NotRequired[
        "capo_elasticsearch_service.types.reservation_token.ReservationToken"
    ]
    """<p>The customer-specified identifier to track this reservation.</p>"""
    reserved_elasticsearch_instance_id: NotRequired[
        "capo_elasticsearch_service.types.guid.GUID"
    ]
    """<p>The unique identifier for the reservation.</p>"""
    reserved_elasticsearch_instance_offering_id: NotRequired[
        "capo_elasticsearch_service.types.string.String"
    ]
    """<p>The offering identifier.</p>"""
    elasticsearch_instance_type: NotRequired[
        "capo_elasticsearch_service.types.es_partition_instance_type.ESPartitionInstanceType"
    ]
    """<p>The Elasticsearch instance type offered by the reserved instance offering.</p>"""
    start_time: NotRequired[
        "capo_elasticsearch_service.types.update_timestamp.UpdateTimestamp"
    ]
    """<p>The time the reservation started.</p>"""
    duration: "capo_elasticsearch_service.types.integer.Integer"
    """<p>The duration, in seconds, for which the Elasticsearch instance is reserved.</p>"""
    fixed_price: NotRequired["capo_elasticsearch_service.types.double.Double"]
    """<p>The upfront fixed charge you will paid to purchase the specific reserved Elasticsearch instance offering. </p>"""
    usage_price: NotRequired["capo_elasticsearch_service.types.double.Double"]
    """<p>The rate you are charged for each hour for the domain that is using this reserved instance.</p>"""
    currency_code: NotRequired["capo_elasticsearch_service.types.string.String"]
    """<p>The currency code for the reserved Elasticsearch instance offering.</p>"""
    elasticsearch_instance_count: "capo_elasticsearch_service.types.integer.Integer"
    """<p>The number of Elasticsearch instances that have been reserved.</p>"""
    state: NotRequired["capo_elasticsearch_service.types.string.String"]
    """<p>The state of the reserved Elasticsearch instance.</p>"""
    payment_option: NotRequired[
        "capo_elasticsearch_service.types.reserved_elasticsearch_instance_payment_option.ReservedElasticsearchInstancePaymentOption"
    ]
    """<p>The payment option as defined in the reserved Elasticsearch instance offering.</p>"""
    recurring_charges: NotRequired[
        "capo_elasticsearch_service.types.recurring_charge_list.RecurringChargeList"
    ]
    """<p>The charge to your account regardless of whether you are creating any domains using the instance offering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReservedElasticsearchInstance) -> dict:
    out: dict = {}
    if "reservation_name" in value:
        out["ReservationName"] = value["reservation_name"]
    if "reserved_elasticsearch_instance_id" in value:
        out["ReservedElasticsearchInstanceId"] = value[
            "reserved_elasticsearch_instance_id"
        ]
    if "reserved_elasticsearch_instance_offering_id" in value:
        out["ReservedElasticsearchInstanceOfferingId"] = value[
            "reserved_elasticsearch_instance_offering_id"
        ]
    if "elasticsearch_instance_type" in value:
        import capo_elasticsearch_service.types.es_partition_instance_type

        out["ElasticsearchInstanceType"] = (
            capo_elasticsearch_service.types.es_partition_instance_type.serialize_json(
                value["elasticsearch_instance_type"]
            )
        )
    if "start_time" in value:
        import capo_elasticsearch_service.types.update_timestamp

        out["StartTime"] = (
            capo_elasticsearch_service.types.update_timestamp.serialize_json(
                value["start_time"]
            )
        )
    out["Duration"] = value.get("duration", 0)
    if "fixed_price" in value:
        out["FixedPrice"] = value["fixed_price"]
    if "usage_price" in value:
        out["UsagePrice"] = value["usage_price"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    out["ElasticsearchInstanceCount"] = value.get("elasticsearch_instance_count", 0)
    if "state" in value:
        out["State"] = value["state"]
    if "payment_option" in value:
        import capo_elasticsearch_service.types.reserved_elasticsearch_instance_payment_option

        out["PaymentOption"] = (
            capo_elasticsearch_service.types.reserved_elasticsearch_instance_payment_option.serialize_json(
                value["payment_option"]
            )
        )
    if "recurring_charges" in value:
        import capo_elasticsearch_service.types.recurring_charge_list

        out["RecurringCharges"] = (
            capo_elasticsearch_service.types.recurring_charge_list.serialize_json(
                value["recurring_charges"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReservedElasticsearchInstance:
    out: ReservedElasticsearchInstance = {}  # type: ignore[typeddict-item]
    if "ReservationName" in data:
        out["reservation_name"] = data["ReservationName"]
    if "ReservedElasticsearchInstanceId" in data:
        out["reserved_elasticsearch_instance_id"] = data[
            "ReservedElasticsearchInstanceId"
        ]
    if "ReservedElasticsearchInstanceOfferingId" in data:
        out["reserved_elasticsearch_instance_offering_id"] = data[
            "ReservedElasticsearchInstanceOfferingId"
        ]
    if "ElasticsearchInstanceType" in data:
        import capo_elasticsearch_service.types.es_partition_instance_type

        out["elasticsearch_instance_type"] = (
            capo_elasticsearch_service.types.es_partition_instance_type.deserialize_json(
                data["ElasticsearchInstanceType"]
            )
        )
    if "StartTime" in data:
        import capo_elasticsearch_service.types.update_timestamp

        out["start_time"] = (
            capo_elasticsearch_service.types.update_timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if "FixedPrice" in data:
        out["fixed_price"] = data["FixedPrice"]
    if "UsagePrice" in data:
        out["usage_price"] = data["UsagePrice"]
    if "CurrencyCode" in data:
        out["currency_code"] = data["CurrencyCode"]
    if "ElasticsearchInstanceCount" in data:
        out["elasticsearch_instance_count"] = data["ElasticsearchInstanceCount"]
    else:
        out["elasticsearch_instance_count"] = 0
    if "State" in data:
        out["state"] = data["State"]
    if "PaymentOption" in data:
        import capo_elasticsearch_service.types.reserved_elasticsearch_instance_payment_option

        out["payment_option"] = (
            capo_elasticsearch_service.types.reserved_elasticsearch_instance_payment_option.deserialize_json(
                data["PaymentOption"]
            )
        )
    if "RecurringCharges" in data:
        import capo_elasticsearch_service.types.recurring_charge_list

        out["recurring_charges"] = (
            capo_elasticsearch_service.types.recurring_charge_list.deserialize_json(
                data["RecurringCharges"]
            )
        )
    return out
