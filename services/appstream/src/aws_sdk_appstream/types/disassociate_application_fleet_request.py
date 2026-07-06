"""Generated from Smithy shape ``com.amazonaws.appstream#DisassociateApplicationFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.arn
    import aws_sdk_appstream.types.name


class DisassociateApplicationFleetRequest(TypedDict, closed=True):
    fleet_name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the fleet.</p>"""
    application_arn: NotRequired["aws_sdk_appstream.types.arn.Arn"]
    """<p>The ARN of the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateApplicationFleetRequest) -> dict:
    out: dict = {}
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateApplicationFleetRequest:
    out: DisassociateApplicationFleetRequest = {}  # type: ignore[typeddict-item]
    if "FleetName" in data:
        out["fleet_name"] = data["FleetName"]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    return out
