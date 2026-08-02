"""Generated from Smithy shape ``com.amazonaws.ec2#ExportClientVpnClientConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class ExportClientVpnClientConfigurationResult(TypedDict, closed=True):
    client_configuration: NotRequired["capo_ec2.types.string.String"]
    """<p>The contents of the Client VPN endpoint configuration file.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportClientVpnClientConfigurationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_configuration" in value:
        pairs.append(
            (f"{key_prefix}ClientConfiguration", str(value["client_configuration"]))
        )


def deserialize_ec2_query(el: Element) -> ExportClientVpnClientConfigurationResult:
    out: ExportClientVpnClientConfigurationResult = {}  # type: ignore[typeddict-item]
    child_client_configuration = el.find("ClientConfiguration")
    if child_client_configuration is not None:
        out["client_configuration"] = str(child_client_configuration.text or "")
    return out
