"""Generated from Smithy shape ``com.amazonaws.costexplorer#RDSInstanceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_boolean
    import aws_sdk_cost_explorer.types.generic_string


class RDSInstanceDetails(TypedDict, closed=True):
    family: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The instance family of the recommended reservation.</p>"""
    instance_type: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The type of instance that Amazon Web Services recommends.</p>"""
    region: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The Amazon Web Services Region of the recommended reservation.</p>"""
    database_engine: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The database engine that the recommended reservation supports.</p>"""
    database_edition: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The database edition that the recommended reservation supports.</p>"""
    deployment_option: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>Determines whether the recommendation is for a reservation in a single Availability Zone or a reservation with a backup in a second Availability Zone.</p>"""
    license_model: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The license model that the recommended reservation supports.</p>"""
    current_generation: "aws_sdk_cost_explorer.types.generic_boolean.GenericBoolean"
    """<p>Determines whether the recommendation is for a current-generation instance. </p>"""
    size_flex_eligible: "aws_sdk_cost_explorer.types.generic_boolean.GenericBoolean"
    """<p>Determines whether the recommended reservation is size flexible.</p>"""
    deployment_model: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>Determines whether the recommendation is for a reservation for RDS Custom.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RDSInstanceDetails) -> dict:
    out: dict = {}
    if "family" in value:
        out["Family"] = value["family"]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "region" in value:
        out["Region"] = value["region"]
    if "database_engine" in value:
        out["DatabaseEngine"] = value["database_engine"]
    if "database_edition" in value:
        out["DatabaseEdition"] = value["database_edition"]
    if "deployment_option" in value:
        out["DeploymentOption"] = value["deployment_option"]
    if "license_model" in value:
        out["LicenseModel"] = value["license_model"]
    out["CurrentGeneration"] = value.get("current_generation", False)
    out["SizeFlexEligible"] = value.get("size_flex_eligible", False)
    if "deployment_model" in value:
        out["DeploymentModel"] = value["deployment_model"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RDSInstanceDetails:
    out: RDSInstanceDetails = {}  # type: ignore[typeddict-item]
    if "Family" in data:
        out["family"] = data["Family"]
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "Region" in data:
        out["region"] = data["Region"]
    if "DatabaseEngine" in data:
        out["database_engine"] = data["DatabaseEngine"]
    if "DatabaseEdition" in data:
        out["database_edition"] = data["DatabaseEdition"]
    if "DeploymentOption" in data:
        out["deployment_option"] = data["DeploymentOption"]
    if "LicenseModel" in data:
        out["license_model"] = data["LicenseModel"]
    if "CurrentGeneration" in data:
        out["current_generation"] = data["CurrentGeneration"]
    else:
        out["current_generation"] = False
    if "SizeFlexEligible" in data:
        out["size_flex_eligible"] = data["SizeFlexEligible"]
    else:
        out["size_flex_eligible"] = False
    if "DeploymentModel" in data:
        out["deployment_model"] = data["DeploymentModel"]
    return out
