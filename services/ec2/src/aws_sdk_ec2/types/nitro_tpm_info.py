"""Generated from Smithy shape ``com.amazonaws.ec2#NitroTpmInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.nitro_tpm_supported_versions_list


class NitroTpmInfo(TypedDict, closed=True):
    supported_versions: NotRequired[
        "aws_sdk_ec2.types.nitro_tpm_supported_versions_list.NitroTpmSupportedVersionsList"
    ]
    """<p>Indicates the supported NitroTPM versions.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NitroTpmInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "supported_versions" in value:
        import aws_sdk_ec2.types.nitro_tpm_supported_versions_list

        aws_sdk_ec2.types.nitro_tpm_supported_versions_list.serialize_ec2_query(
            value["supported_versions"], pairs, f"{prefix}.SupportedVersions"
        )


def deserialize_ec2_query(el: Element) -> NitroTpmInfo:
    out: NitroTpmInfo = {}  # type: ignore[typeddict-item]
    if el.find("SupportedVersions") is not None:
        import aws_sdk_ec2.types.nitro_tpm_supported_versions_list

        out["supported_versions"] = (
            aws_sdk_ec2.types.nitro_tpm_supported_versions_list.deserialize_ec2_query(
                el, "SupportedVersions"
            )
        )
    return out
