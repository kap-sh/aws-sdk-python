"""Generated from Smithy shape ``com.amazonaws.ec2#RecurringChargesList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.recurring_charge

RecurringChargesList: TypeAlias = list[
    "aws_sdk_ec2.types.recurring_charge.RecurringCharge"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RecurringChargesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.recurring_charge

        aws_sdk_ec2.types.recurring_charge.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> RecurringChargesList:
    import aws_sdk_ec2.types.recurring_charge

    out: RecurringChargesList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.recurring_charge.deserialize_ec2_query(child))
    return out
