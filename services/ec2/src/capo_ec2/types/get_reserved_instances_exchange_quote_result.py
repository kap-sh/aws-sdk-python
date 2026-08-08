"""Generated from Smithy shape ``com.amazonaws.ec2#GetReservedInstancesExchangeQuoteResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.reservation_value
    import capo_ec2.types.reserved_instance_reservation_value_set
    import capo_ec2.types.string
    import capo_ec2.types.target_reservation_value_set


class GetReservedInstancesExchangeQuoteResult(TypedDict, closed=True):
    currency_code: NotRequired["capo_ec2.types.string.String"]
    """<p>The currency of the transaction.</p>"""
    is_valid_exchange: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, the exchange is valid. If <code>false</code>, the exchange cannot be completed.</p>"""
    output_reserved_instances_will_expire_at: NotRequired[
        "capo_ec2.types.date_time.DateTime"
    ]
    """<p>The new end date of the reservation term.</p>"""
    payment_due: NotRequired["capo_ec2.types.string.String"]
    """<p>The total true upfront charge for the exchange.</p>"""
    reserved_instance_value_rollup: NotRequired[
        "capo_ec2.types.reservation_value.ReservationValue"
    ]
    """<p>The cost associated with the Reserved Instance.</p>"""
    reserved_instance_value_set: NotRequired[
        "capo_ec2.types.reserved_instance_reservation_value_set.ReservedInstanceReservationValueSet"
    ]
    """<p>The configuration of your Convertible Reserved Instances.</p>"""
    target_configuration_value_rollup: NotRequired[
        "capo_ec2.types.reservation_value.ReservationValue"
    ]
    """<p>The cost associated with the Reserved Instance.</p>"""
    target_configuration_value_set: NotRequired[
        "capo_ec2.types.target_reservation_value_set.TargetReservationValueSet"
    ]
    """<p>The values of the target Convertible Reserved Instances.</p>"""
    validation_failure_reason: NotRequired["capo_ec2.types.string.String"]
    """<p>Describes the reason why the exchange cannot be completed.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetReservedInstancesExchangeQuoteResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "currency_code" in value:
        pairs.append((f"{key_prefix}CurrencyCode", str(value["currency_code"])))
    if "is_valid_exchange" in value:
        pairs.append(
            (
                f"{key_prefix}IsValidExchange",
                "true" if value["is_valid_exchange"] else "false",
            )
        )
    if "output_reserved_instances_will_expire_at" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["output_reserved_instances_will_expire_at"],
            pairs,
            f"{key_prefix}OutputReservedInstancesWillExpireAt",
        )
    if "payment_due" in value:
        pairs.append((f"{key_prefix}PaymentDue", str(value["payment_due"])))
    if "reserved_instance_value_rollup" in value:
        import capo_ec2.types.reservation_value

        capo_ec2.types.reservation_value.serialize_ec2_query(
            value["reserved_instance_value_rollup"],
            pairs,
            f"{key_prefix}ReservedInstanceValueRollup",
        )
    if "reserved_instance_value_set" in value:
        import capo_ec2.types.reserved_instance_reservation_value_set

        capo_ec2.types.reserved_instance_reservation_value_set.serialize_ec2_query(
            value["reserved_instance_value_set"],
            pairs,
            f"{key_prefix}ReservedInstanceValueSet",
        )
    if "target_configuration_value_rollup" in value:
        import capo_ec2.types.reservation_value

        capo_ec2.types.reservation_value.serialize_ec2_query(
            value["target_configuration_value_rollup"],
            pairs,
            f"{key_prefix}TargetConfigurationValueRollup",
        )
    if "target_configuration_value_set" in value:
        import capo_ec2.types.target_reservation_value_set

        capo_ec2.types.target_reservation_value_set.serialize_ec2_query(
            value["target_configuration_value_set"],
            pairs,
            f"{key_prefix}TargetConfigurationValueSet",
        )
    if "validation_failure_reason" in value:
        pairs.append(
            (
                f"{key_prefix}ValidationFailureReason",
                str(value["validation_failure_reason"]),
            )
        )


def deserialize_ec2_query(el: Element) -> GetReservedInstancesExchangeQuoteResult:
    out: GetReservedInstancesExchangeQuoteResult = {}  # type: ignore[typeddict-item]
    child_currency_code = el.find("currencyCode")
    if child_currency_code is not None:
        out["currency_code"] = str(child_currency_code.text or "")
    child_is_valid_exchange = el.find("isValidExchange")
    if child_is_valid_exchange is not None:
        out["is_valid_exchange"] = (
            child_is_valid_exchange.text or ""
        ).lower() == "true"
    child_output_reserved_instances_will_expire_at = el.find(
        "outputReservedInstancesWillExpireAt"
    )
    if child_output_reserved_instances_will_expire_at is not None:
        import capo_ec2.types.date_time

        out["output_reserved_instances_will_expire_at"] = (
            capo_ec2.types.date_time.deserialize_ec2_query(
                child_output_reserved_instances_will_expire_at
            )
        )
    child_payment_due = el.find("paymentDue")
    if child_payment_due is not None:
        out["payment_due"] = str(child_payment_due.text or "")
    child_reserved_instance_value_rollup = el.find("reservedInstanceValueRollup")
    if child_reserved_instance_value_rollup is not None:
        import capo_ec2.types.reservation_value

        out["reserved_instance_value_rollup"] = (
            capo_ec2.types.reservation_value.deserialize_ec2_query(
                child_reserved_instance_value_rollup
            )
        )
    if el.find("reservedInstanceValueSet") is not None:
        import capo_ec2.types.reserved_instance_reservation_value_set

        out["reserved_instance_value_set"] = (
            capo_ec2.types.reserved_instance_reservation_value_set.deserialize_ec2_query(
                el, "reservedInstanceValueSet"
            )
        )
    child_target_configuration_value_rollup = el.find("targetConfigurationValueRollup")
    if child_target_configuration_value_rollup is not None:
        import capo_ec2.types.reservation_value

        out["target_configuration_value_rollup"] = (
            capo_ec2.types.reservation_value.deserialize_ec2_query(
                child_target_configuration_value_rollup
            )
        )
    if el.find("targetConfigurationValueSet") is not None:
        import capo_ec2.types.target_reservation_value_set

        out["target_configuration_value_set"] = (
            capo_ec2.types.target_reservation_value_set.deserialize_ec2_query(
                el, "targetConfigurationValueSet"
            )
        )
    child_validation_failure_reason = el.find("validationFailureReason")
    if child_validation_failure_reason is not None:
        out["validation_failure_reason"] = str(
            child_validation_failure_reason.text or ""
        )
    return out
