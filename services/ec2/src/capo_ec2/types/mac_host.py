"""Generated from Smithy shape ``com.amazonaws.ec2#MacHost``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.dedicated_host_id
    import capo_ec2.types.mac_os_version_string_list


class MacHost(TypedDict, closed=True):
    host_id: NotRequired["capo_ec2.types.dedicated_host_id.DedicatedHostId"]
    """<p> The EC2 Mac Dedicated Host ID. </p>"""
    mac_os_latest_supported_versions: NotRequired[
        "capo_ec2.types.mac_os_version_string_list.MacOSVersionStringList"
    ]
    """<p> The latest macOS versions that the EC2 Mac Dedicated Host can launch without being upgraded. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MacHost, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "host_id" in value:
        pairs.append((f"{prefix}.HostId", str(value["host_id"])))
    if "mac_os_latest_supported_versions" in value:
        import capo_ec2.types.mac_os_version_string_list

        capo_ec2.types.mac_os_version_string_list.serialize_ec2_query(
            value["mac_os_latest_supported_versions"],
            pairs,
            f"{prefix}.MacOSLatestSupportedVersionSet",
        )


def deserialize_ec2_query(el: Element) -> MacHost:
    out: MacHost = {}  # type: ignore[typeddict-item]
    child_host_id = el.find("HostId")
    if child_host_id is not None:
        out["host_id"] = str(child_host_id.text or "")
    if el.find("MacOSLatestSupportedVersionSet") is not None:
        import capo_ec2.types.mac_os_version_string_list

        out["mac_os_latest_supported_versions"] = (
            capo_ec2.types.mac_os_version_string_list.deserialize_ec2_query(
                el, "MacOSLatestSupportedVersionSet"
            )
        )
    return out
