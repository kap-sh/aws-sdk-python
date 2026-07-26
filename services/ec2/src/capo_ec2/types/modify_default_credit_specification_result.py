"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyDefaultCreditSpecificationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_family_credit_specification


class ModifyDefaultCreditSpecificationResult(TypedDict, closed=True):
    instance_family_credit_specification: NotRequired[
        "capo_ec2.types.instance_family_credit_specification.InstanceFamilyCreditSpecification"
    ]
    """<p>The default credit option for CPU usage of the instance family.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyDefaultCreditSpecificationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_family_credit_specification" in value:
        import capo_ec2.types.instance_family_credit_specification

        capo_ec2.types.instance_family_credit_specification.serialize_ec2_query(
            value["instance_family_credit_specification"],
            pairs,
            f"{prefix}.InstanceFamilyCreditSpecification",
        )


def deserialize_ec2_query(el: Element) -> ModifyDefaultCreditSpecificationResult:
    out: ModifyDefaultCreditSpecificationResult = {}  # type: ignore[typeddict-item]
    child_instance_family_credit_specification = el.find(
        "InstanceFamilyCreditSpecification"
    )
    if child_instance_family_credit_specification is not None:
        import capo_ec2.types.instance_family_credit_specification

        out["instance_family_credit_specification"] = (
            capo_ec2.types.instance_family_credit_specification.deserialize_ec2_query(
                child_instance_family_credit_specification
            )
        )
    return out
