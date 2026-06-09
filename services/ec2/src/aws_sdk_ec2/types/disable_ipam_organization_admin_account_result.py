"""Generated from Smithy shape ``com.amazonaws.ec2#DisableIpamOrganizationAdminAccountResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class DisableIpamOrganizationAdminAccountResult(TypedDict):
    success: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The result of disabling the IPAM account.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableIpamOrganizationAdminAccountResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "success" in value:
        pairs.append((f"{prefix}.Success", "true" if value["success"] else "false"))


def deserialize_ec2_query(el: Element) -> DisableIpamOrganizationAdminAccountResult:
    out: DisableIpamOrganizationAdminAccountResult = {}  # type: ignore[typeddict-item]
    child_success = el.find("Success")
    if child_success is not None:
        out["success"] = (child_success.text or "").lower() == "true"
    return out
