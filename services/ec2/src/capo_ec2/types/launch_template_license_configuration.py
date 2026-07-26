"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateLicenseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class LaunchTemplateLicenseConfiguration(TypedDict, closed=True):
    license_configuration_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the license configuration.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateLicenseConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "license_configuration_arn" in value:
        pairs.append(
            (
                f"{prefix}.LicenseConfigurationArn",
                str(value["license_configuration_arn"]),
            )
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateLicenseConfiguration:
    out: LaunchTemplateLicenseConfiguration = {}  # type: ignore[typeddict-item]
    child_license_configuration_arn = el.find("LicenseConfigurationArn")
    if child_license_configuration_arn is not None:
        out["license_configuration_arn"] = str(
            child_license_configuration_arn.text or ""
        )
    return out
