"""Generated from Smithy shape ``com.amazonaws.ec2#ClientLoginBannerOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string


class ClientLoginBannerOptions(TypedDict, closed=True):
    enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Enable or disable a customizable text banner that will be displayed on Amazon Web Services provided clients when a VPN session is established.</p> <p>Valid values: <code>true | false</code> </p> <p>Default value: <code>false</code> </p>"""
    banner_text: NotRequired["capo_ec2.types.string.String"]
    """<p>Customizable text that will be displayed in a banner on Amazon Web Services provided clients when a VPN session is established. UTF-8 encoded characters only. Maximum of 1400 characters.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientLoginBannerOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "enabled" in value:
        pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))
    if "banner_text" in value:
        pairs.append((f"{key_prefix}BannerText", str(value["banner_text"])))


def deserialize_ec2_query(el: Element) -> ClientLoginBannerOptions:
    out: ClientLoginBannerOptions = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_banner_text = el.find("BannerText")
    if child_banner_text is not None:
        out["banner_text"] = str(child_banner_text.text or "")
    return out
