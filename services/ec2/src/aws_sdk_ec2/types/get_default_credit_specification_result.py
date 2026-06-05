"""Generated from Smithy shape ``com.amazonaws.ec2#GetDefaultCreditSpecificationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_family_credit_specification


class GetDefaultCreditSpecificationResult(TypedDict):
    instance_family_credit_specification: NotRequired[
        "aws_sdk_ec2.types.instance_family_credit_specification.InstanceFamilyCreditSpecification"
    ]
    """<p>The default credit option for CPU usage of the instance family.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetDefaultCreditSpecificationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_family_credit_specification" in value:
        import aws_sdk_ec2.types.instance_family_credit_specification

        aws_sdk_ec2.types.instance_family_credit_specification.serialize_ec2_query(
            value["instance_family_credit_specification"],
            pairs,
            f"{prefix}.InstanceFamilyCreditSpecification",
        )


def deserialize_ec2_query(el: Element) -> GetDefaultCreditSpecificationResult:
    out: GetDefaultCreditSpecificationResult = {}  # type: ignore[typeddict-item]
    child_instance_family_credit_specification = el.find(
        "InstanceFamilyCreditSpecification"
    )
    if child_instance_family_credit_specification is not None:
        import aws_sdk_ec2.types.instance_family_credit_specification

        out["instance_family_credit_specification"] = (
            aws_sdk_ec2.types.instance_family_credit_specification.deserialize_ec2_query(
                child_instance_family_credit_specification
            )
        )
    return out
