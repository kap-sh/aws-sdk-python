"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ReservedElasticsearchInstanceOffering``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.double
    import aws_sdk_elasticsearch_service.types.es_partition_instance_type
    import aws_sdk_elasticsearch_service.types.guid
    import aws_sdk_elasticsearch_service.types.integer
    import aws_sdk_elasticsearch_service.types.recurring_charge_list
    import aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_payment_option
    import aws_sdk_elasticsearch_service.types.string


class ReservedElasticsearchInstanceOffering(TypedDict):
    reserved_elasticsearch_instance_offering_id: NotRequired[
        "aws_sdk_elasticsearch_service.types.guid.GUID"
    ]
    """<p>The Elasticsearch reserved instance offering identifier.</p>"""
    elasticsearch_instance_type: NotRequired[
        "aws_sdk_elasticsearch_service.types.es_partition_instance_type.ESPartitionInstanceType"
    ]
    """<p>The Elasticsearch instance type offered by the reserved instance offering.</p>"""
    duration: "aws_sdk_elasticsearch_service.types.integer.Integer"
    """<p>The duration, in seconds, for which the offering will reserve the Elasticsearch instance.</p>"""
    fixed_price: NotRequired["aws_sdk_elasticsearch_service.types.double.Double"]
    """<p>The upfront fixed charge you will pay to purchase the specific reserved Elasticsearch instance offering. </p>"""
    usage_price: NotRequired["aws_sdk_elasticsearch_service.types.double.Double"]
    """<p>The rate you are charged for each hour the domain that is using the offering is running.</p>"""
    currency_code: NotRequired["aws_sdk_elasticsearch_service.types.string.String"]
    """<p>The currency code for the reserved Elasticsearch instance offering.</p>"""
    payment_option: NotRequired[
        "aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_payment_option.ReservedElasticsearchInstancePaymentOption"
    ]
    """<p>Payment option for the reserved Elasticsearch instance offering</p>"""
    recurring_charges: NotRequired[
        "aws_sdk_elasticsearch_service.types.recurring_charge_list.RecurringChargeList"
    ]
    """<p>The charge to your account regardless of whether you are creating any domains using the instance offering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReservedElasticsearchInstanceOffering) -> dict:
    out: dict = {}
    if "reserved_elasticsearch_instance_offering_id" in value:
        out["ReservedElasticsearchInstanceOfferingId"] = value[
            "reserved_elasticsearch_instance_offering_id"
        ]
    if "elasticsearch_instance_type" in value:
        import aws_sdk_elasticsearch_service.types.es_partition_instance_type

        out["ElasticsearchInstanceType"] = (
            aws_sdk_elasticsearch_service.types.es_partition_instance_type.serialize_json(
                value["elasticsearch_instance_type"]
            )
        )
    out["Duration"] = value.get("duration", 0)
    if "fixed_price" in value:
        out["FixedPrice"] = value["fixed_price"]
    if "usage_price" in value:
        out["UsagePrice"] = value["usage_price"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    if "payment_option" in value:
        import aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_payment_option

        out["PaymentOption"] = (
            aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_payment_option.serialize_json(
                value["payment_option"]
            )
        )
    if "recurring_charges" in value:
        import aws_sdk_elasticsearch_service.types.recurring_charge_list

        out["RecurringCharges"] = (
            aws_sdk_elasticsearch_service.types.recurring_charge_list.serialize_json(
                value["recurring_charges"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReservedElasticsearchInstanceOffering:
    out: ReservedElasticsearchInstanceOffering = {}  # type: ignore[typeddict-item]
    if "ReservedElasticsearchInstanceOfferingId" in data:
        out["reserved_elasticsearch_instance_offering_id"] = data[
            "ReservedElasticsearchInstanceOfferingId"
        ]
    if "ElasticsearchInstanceType" in data:
        import aws_sdk_elasticsearch_service.types.es_partition_instance_type

        out["elasticsearch_instance_type"] = (
            aws_sdk_elasticsearch_service.types.es_partition_instance_type.deserialize_json(
                data["ElasticsearchInstanceType"]
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
    if "PaymentOption" in data:
        import aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_payment_option

        out["payment_option"] = (
            aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_payment_option.deserialize_json(
                data["PaymentOption"]
            )
        )
    if "RecurringCharges" in data:
        import aws_sdk_elasticsearch_service.types.recurring_charge_list

        out["recurring_charges"] = (
            aws_sdk_elasticsearch_service.types.recurring_charge_list.deserialize_json(
                data["RecurringCharges"]
            )
        )
    return out
