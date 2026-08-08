"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceCreditSpecificationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.successful_instance_credit_specification_set
    import capo_ec2.types.unsuccessful_instance_credit_specification_set


class ModifyInstanceCreditSpecificationResult(TypedDict, closed=True):
    successful_instance_credit_specifications: NotRequired[
        "capo_ec2.types.successful_instance_credit_specification_set.SuccessfulInstanceCreditSpecificationSet"
    ]
    """<p>Information about the instances whose credit option for CPU usage was successfully modified.</p>"""
    unsuccessful_instance_credit_specifications: NotRequired[
        "capo_ec2.types.unsuccessful_instance_credit_specification_set.UnsuccessfulInstanceCreditSpecificationSet"
    ]
    """<p>Information about the instances whose credit option for CPU usage was not modified.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceCreditSpecificationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "successful_instance_credit_specifications" in value:
        import capo_ec2.types.successful_instance_credit_specification_set

        capo_ec2.types.successful_instance_credit_specification_set.serialize_ec2_query(
            value["successful_instance_credit_specifications"],
            pairs,
            f"{key_prefix}SuccessfulInstanceCreditSpecificationSet",
        )
    if "unsuccessful_instance_credit_specifications" in value:
        import capo_ec2.types.unsuccessful_instance_credit_specification_set

        capo_ec2.types.unsuccessful_instance_credit_specification_set.serialize_ec2_query(
            value["unsuccessful_instance_credit_specifications"],
            pairs,
            f"{key_prefix}UnsuccessfulInstanceCreditSpecificationSet",
        )


def deserialize_ec2_query(el: Element) -> ModifyInstanceCreditSpecificationResult:
    out: ModifyInstanceCreditSpecificationResult = {}  # type: ignore[typeddict-item]
    if el.find("successfulInstanceCreditSpecificationSet") is not None:
        import capo_ec2.types.successful_instance_credit_specification_set

        out["successful_instance_credit_specifications"] = (
            capo_ec2.types.successful_instance_credit_specification_set.deserialize_ec2_query(
                el, "successfulInstanceCreditSpecificationSet"
            )
        )
    if el.find("unsuccessfulInstanceCreditSpecificationSet") is not None:
        import capo_ec2.types.unsuccessful_instance_credit_specification_set

        out["unsuccessful_instance_credit_specifications"] = (
            capo_ec2.types.unsuccessful_instance_credit_specification_set.deserialize_ec2_query(
                el, "unsuccessfulInstanceCreditSpecificationSet"
            )
        )
    return out
