"""Generated from Smithy shape ``com.amazonaws.ec2#DisableIpamOrganizationAdminAccountResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class DisableIpamOrganizationAdminAccountResult(TypedDict, closed=True):
    success: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>The result of disabling the IPAM account.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableIpamOrganizationAdminAccountResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "success" in value:
        pairs.append((f"{key_prefix}Success", "true" if value["success"] else "false"))


def deserialize_ec2_query(el: Element) -> DisableIpamOrganizationAdminAccountResult:
    out: DisableIpamOrganizationAdminAccountResult = {}  # type: ignore[typeddict-item]
    child_success = el.find("Success")
    if child_success is not None:
        out["success"] = (child_success.text or "").lower() == "true"
    return out
