"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceCreditSpecificationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.successful_instance_credit_specification_set
    import aws_sdk_ec2.types.unsuccessful_instance_credit_specification_set


class ModifyInstanceCreditSpecificationResult(TypedDict):
    successful_instance_credit_specifications: NotRequired[
        "aws_sdk_ec2.types.successful_instance_credit_specification_set.SuccessfulInstanceCreditSpecificationSet"
    ]
    """<p>Information about the instances whose credit option for CPU usage was successfully modified.</p>"""
    unsuccessful_instance_credit_specifications: NotRequired[
        "aws_sdk_ec2.types.unsuccessful_instance_credit_specification_set.UnsuccessfulInstanceCreditSpecificationSet"
    ]
    """<p>Information about the instances whose credit option for CPU usage was not modified.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceCreditSpecificationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "successful_instance_credit_specifications" in value:
        import aws_sdk_ec2.types.successful_instance_credit_specification_set

        aws_sdk_ec2.types.successful_instance_credit_specification_set.serialize_ec2_query(
            value["successful_instance_credit_specifications"],
            pairs,
            f"{prefix}.SuccessfulInstanceCreditSpecificationSet",
        )
    if "unsuccessful_instance_credit_specifications" in value:
        import aws_sdk_ec2.types.unsuccessful_instance_credit_specification_set

        aws_sdk_ec2.types.unsuccessful_instance_credit_specification_set.serialize_ec2_query(
            value["unsuccessful_instance_credit_specifications"],
            pairs,
            f"{prefix}.UnsuccessfulInstanceCreditSpecificationSet",
        )


def deserialize_ec2_query(el: Element) -> ModifyInstanceCreditSpecificationResult:
    out: ModifyInstanceCreditSpecificationResult = {}  # type: ignore[typeddict-item]
    if el.find("SuccessfulInstanceCreditSpecificationSet") is not None:
        import aws_sdk_ec2.types.successful_instance_credit_specification_set

        out["successful_instance_credit_specifications"] = (
            aws_sdk_ec2.types.successful_instance_credit_specification_set.deserialize_ec2_query(
                el, "SuccessfulInstanceCreditSpecificationSet"
            )
        )
    if el.find("UnsuccessfulInstanceCreditSpecificationSet") is not None:
        import aws_sdk_ec2.types.unsuccessful_instance_credit_specification_set

        out["unsuccessful_instance_credit_specifications"] = (
            aws_sdk_ec2.types.unsuccessful_instance_credit_specification_set.deserialize_ec2_query(
                el, "UnsuccessfulInstanceCreditSpecificationSet"
            )
        )
    return out
