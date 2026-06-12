"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRegionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean


class GetRegionsRequest(TypedDict):
    include_availability_zones: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether to also include Availability Zones in your get regions request. Availability Zones are indicated with a letter: <code>us-east-2a</code>.</p>"""
    include_relational_database_availability_zones: NotRequired[
        "aws_sdk_lightsail.types.boolean.boolean"
    ]
    """<p>A Boolean value indicating whether to also include Availability Zones for databases in your get regions request. Availability Zones are indicated with a letter (<code>us-east-2a</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRegionsRequest) -> dict:
    out: dict = {}
    if "include_availability_zones" in value:
        out["includeAvailabilityZones"] = value["include_availability_zones"]
    if "include_relational_database_availability_zones" in value:
        out["includeRelationalDatabaseAvailabilityZones"] = value[
            "include_relational_database_availability_zones"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRegionsRequest:
    out: GetRegionsRequest = {}  # type: ignore[typeddict-item]
    if "includeAvailabilityZones" in data:
        out["include_availability_zones"] = data["includeAvailabilityZones"]
    if "includeRelationalDatabaseAvailabilityZones" in data:
        out["include_relational_database_availability_zones"] = data[
            "includeRelationalDatabaseAvailabilityZones"
        ]
    return out
