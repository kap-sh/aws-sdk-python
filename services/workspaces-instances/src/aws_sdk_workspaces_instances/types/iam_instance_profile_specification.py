"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#IamInstanceProfileSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.arn
    import aws_sdk_workspaces_instances.types.string64


class IamInstanceProfileSpecification(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_workspaces_instances.types.arn.ARN"]
    """<p>Amazon Resource Name (ARN) of the IAM instance profile.</p>"""
    name: NotRequired["aws_sdk_workspaces_instances.types.string64.String64"]
    """<p>Name of the IAM instance profile.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IamInstanceProfileSpecification) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IamInstanceProfileSpecification:
    out: IamInstanceProfileSpecification = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
