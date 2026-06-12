"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails(TypedDict):
    hostname: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The hostname to use in the <b>/etc/hosts</b> entry.</p>"""
    ip_address: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The IP address to use in the <b>/etc/hosts</b> entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails,
) -> dict:
    out: dict = {}
    if "hostname" in value:
        out["Hostname"] = value["hostname"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails = {}  # type: ignore[typeddict-item]
    if "Hostname" in data:
        out["hostname"] = data["Hostname"]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    return out
