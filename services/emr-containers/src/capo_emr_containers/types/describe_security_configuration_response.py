"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DescribeSecurityConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.security_configuration


class DescribeSecurityConfigurationResponse(TypedDict, closed=True):
    security_configuration: NotRequired[
        "capo_emr_containers.types.security_configuration.SecurityConfiguration"
    ]
    """<p>Details of the security configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSecurityConfigurationResponse) -> dict:
    out: dict = {}
    if "security_configuration" in value:
        import capo_emr_containers.types.security_configuration

        out["securityConfiguration"] = (
            capo_emr_containers.types.security_configuration.serialize_json(
                value["security_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeSecurityConfigurationResponse:
    out: DescribeSecurityConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "securityConfiguration" in data:
        import capo_emr_containers.types.security_configuration

        out["security_configuration"] = (
            capo_emr_containers.types.security_configuration.deserialize_json(
                data["securityConfiguration"]
            )
        )
    return out
