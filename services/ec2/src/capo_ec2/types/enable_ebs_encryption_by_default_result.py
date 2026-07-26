"""Generated from Smithy shape ``com.amazonaws.ec2#EnableEbsEncryptionByDefaultResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class EnableEbsEncryptionByDefaultResult(TypedDict, closed=True):
    ebs_encryption_by_default: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>The updated status of encryption by default.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableEbsEncryptionByDefaultResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ebs_encryption_by_default" in value:
        pairs.append(
            (
                f"{prefix}.EbsEncryptionByDefault",
                "true" if value["ebs_encryption_by_default"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> EnableEbsEncryptionByDefaultResult:
    out: EnableEbsEncryptionByDefaultResult = {}  # type: ignore[typeddict-item]
    child_ebs_encryption_by_default = el.find("EbsEncryptionByDefault")
    if child_ebs_encryption_by_default is not None:
        out["ebs_encryption_by_default"] = (
            child_ebs_encryption_by_default.text or ""
        ).lower() == "true"
    return out
