"""Generated from Smithy shape ``com.amazonaws.costexplorer#EC2InstanceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_boolean
    import aws_sdk_cost_explorer.types.generic_string


class EC2InstanceDetails(TypedDict, closed=True):
    family: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The instance family of the recommended reservation.</p>"""
    instance_type: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The type of instance that Amazon Web Services recommends.</p>"""
    region: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The Amazon Web Services Region of the recommended reservation.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The Availability Zone of the recommended reservation.</p>"""
    platform: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The platform of the recommended reservation. The platform is the specific combination of operating system, license model, and software on an instance.</p>"""
    tenancy: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>Determines whether the recommended reservation is dedicated or shared.</p>"""
    current_generation: "aws_sdk_cost_explorer.types.generic_boolean.GenericBoolean"
    """<p>Determines whether the recommendation is for a current-generation instance. </p>"""
    size_flex_eligible: "aws_sdk_cost_explorer.types.generic_boolean.GenericBoolean"
    """<p>Determines whether the recommended reservation is size flexible.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2InstanceDetails) -> dict:
    out: dict = {}
    if "family" in value:
        out["Family"] = value["family"]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "region" in value:
        out["Region"] = value["region"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "platform" in value:
        out["Platform"] = value["platform"]
    if "tenancy" in value:
        out["Tenancy"] = value["tenancy"]
    out["CurrentGeneration"] = value.get("current_generation", False)
    out["SizeFlexEligible"] = value.get("size_flex_eligible", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2InstanceDetails:
    out: EC2InstanceDetails = {}  # type: ignore[typeddict-item]
    if "Family" in data:
        out["family"] = data["Family"]
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "Region" in data:
        out["region"] = data["Region"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "Platform" in data:
        out["platform"] = data["Platform"]
    if "Tenancy" in data:
        out["tenancy"] = data["Tenancy"]
    if "CurrentGeneration" in data:
        out["current_generation"] = data["CurrentGeneration"]
    else:
        out["current_generation"] = False
    if "SizeFlexEligible" in data:
        out["size_flex_eligible"] = data["SizeFlexEligible"]
    else:
        out["size_flex_eligible"] = False
    return out
