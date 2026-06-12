"""Generated from Smithy shape ``com.amazonaws.redshift#RecurringChargeList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.recurring_charge

RecurringChargeList: TypeAlias = list[
    "aws_sdk_redshift.types.recurring_charge.RecurringCharge"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RecurringChargeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.recurring_charge

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.recurring_charge.serialize_query(
            item, pairs, f"{prefix}.RecurringCharge.{n}"
        )


def deserialize_query(el: Element) -> RecurringChargeList:
    import aws_sdk_redshift.types.recurring_charge

    out: RecurringChargeList = []
    for child in el.findall("RecurringCharge"):
        out.append(aws_sdk_redshift.types.recurring_charge.deserialize_query(child))
    return out


def serialize_query_flat(
    value: RecurringChargeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.recurring_charge

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.recurring_charge.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RecurringChargeList:
    import aws_sdk_redshift.types.recurring_charge

    out: RecurringChargeList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.recurring_charge.deserialize_query(child))
    return out
