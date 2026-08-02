"""Generated from Smithy shape ``com.amazonaws.ec2#NitroTpmInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.nitro_tpm_supported_versions_list


class NitroTpmInfo(TypedDict, closed=True):
    supported_versions: NotRequired[
        "capo_ec2.types.nitro_tpm_supported_versions_list.NitroTpmSupportedVersionsList"
    ]
    """<p>Indicates the supported NitroTPM versions.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NitroTpmInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "supported_versions" in value:
        import capo_ec2.types.nitro_tpm_supported_versions_list

        capo_ec2.types.nitro_tpm_supported_versions_list.serialize_ec2_query(
            value["supported_versions"], pairs, f"{key_prefix}SupportedVersions"
        )


def deserialize_ec2_query(el: Element) -> NitroTpmInfo:
    out: NitroTpmInfo = {}  # type: ignore[typeddict-item]
    if el.find("SupportedVersions") is not None:
        import capo_ec2.types.nitro_tpm_supported_versions_list

        out["supported_versions"] = (
            capo_ec2.types.nitro_tpm_supported_versions_list.deserialize_ec2_query(
                el, "SupportedVersions"
            )
        )
    return out
