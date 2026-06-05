"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceCreditSpecificationListRequest``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_credit_specification_request

InstanceCreditSpecificationListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.instance_credit_specification_request.InstanceCreditSpecificationRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceCreditSpecificationListRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.instance_credit_specification_request

        aws_sdk_ec2.types.instance_credit_specification_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> InstanceCreditSpecificationListRequest:
    import aws_sdk_ec2.types.instance_credit_specification_request

    out: InstanceCreditSpecificationListRequest = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.instance_credit_specification_request.deserialize_ec2_query(
                child
            )
        )
    return out
