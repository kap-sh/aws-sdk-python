"""Generated from Smithy shape ``com.amazonaws.workspaces#IDCConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.arn


class IDCConfig(TypedDict, closed=True):
    instance_arn: NotRequired["capo_workspaces.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the identity center instance.</p>"""
    application_arn: NotRequired["capo_workspaces.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IDCConfig) -> dict:
    out: dict = {}
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IDCConfig:
    out: IDCConfig = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    return out
