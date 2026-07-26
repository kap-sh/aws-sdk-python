"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbSubnetGroupSubnetAvailabilityZone``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsRdsDbSubnetGroupSubnetAvailabilityZone(TypedDict, closed=True):
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the Availability Zone for a subnet in the subnet group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbSubnetGroupSubnetAvailabilityZone) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbSubnetGroupSubnetAvailabilityZone:
    out: AwsRdsDbSubnetGroupSubnetAvailabilityZone = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
