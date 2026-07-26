"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcEncryptionControlResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc_encryption_control


class CreateVpcEncryptionControlResult(TypedDict, closed=True):
    vpc_encryption_control: NotRequired[
        "capo_ec2.types.vpc_encryption_control.VpcEncryptionControl"
    ]
    """<p>Information about the VPC Encryption Control configuration.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpcEncryptionControlResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpc_encryption_control" in value:
        import capo_ec2.types.vpc_encryption_control

        capo_ec2.types.vpc_encryption_control.serialize_ec2_query(
            value["vpc_encryption_control"], pairs, f"{prefix}.VpcEncryptionControl"
        )


def deserialize_ec2_query(el: Element) -> CreateVpcEncryptionControlResult:
    out: CreateVpcEncryptionControlResult = {}  # type: ignore[typeddict-item]
    child_vpc_encryption_control = el.find("VpcEncryptionControl")
    if child_vpc_encryption_control is not None:
        import capo_ec2.types.vpc_encryption_control

        out["vpc_encryption_control"] = (
            capo_ec2.types.vpc_encryption_control.deserialize_ec2_query(
                child_vpc_encryption_control
            )
        )
    return out
