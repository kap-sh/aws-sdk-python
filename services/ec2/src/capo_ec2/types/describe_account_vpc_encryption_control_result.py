"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAccountVpcEncryptionControlResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.account_vpc_encryption_control


class DescribeAccountVpcEncryptionControlResult(TypedDict, closed=True):
    account_vpc_encryption_control: NotRequired[
        "capo_ec2.types.account_vpc_encryption_control.AccountVpcEncryptionControl"
    ]
    """<p>Information about the account-level VPC Encryption Control configuration.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeAccountVpcEncryptionControlResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "account_vpc_encryption_control" in value:
        import capo_ec2.types.account_vpc_encryption_control

        capo_ec2.types.account_vpc_encryption_control.serialize_ec2_query(
            value["account_vpc_encryption_control"],
            pairs,
            f"{key_prefix}AccountVpcEncryptionControl",
        )


def deserialize_ec2_query(el: Element) -> DescribeAccountVpcEncryptionControlResult:
    out: DescribeAccountVpcEncryptionControlResult = {}  # type: ignore[typeddict-item]
    child_account_vpc_encryption_control = el.find("accountVpcEncryptionControl")
    if child_account_vpc_encryption_control is not None:
        import capo_ec2.types.account_vpc_encryption_control

        out["account_vpc_encryption_control"] = (
            capo_ec2.types.account_vpc_encryption_control.deserialize_ec2_query(
                child_account_vpc_encryption_control
            )
        )
    return out
