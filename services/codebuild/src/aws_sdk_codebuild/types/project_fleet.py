"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectFleet``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.string


class ProjectFleet(TypedDict):
    fleet_arn: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>Specifies the compute fleet ARN for the build project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectFleet) -> dict:
    out: dict = {}
    if "fleet_arn" in value:
        out["fleetArn"] = value["fleet_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProjectFleet:
    out: ProjectFleet = {}  # type: ignore[typeddict-item]
    if "fleetArn" in data:
        out["fleet_arn"] = data["fleetArn"]
    return out
