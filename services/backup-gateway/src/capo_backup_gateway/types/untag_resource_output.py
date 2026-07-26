"""Generated from Smithy shape ``com.amazonaws.backupgateway#UntagResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.resource_arn


class UntagResourceOutput(TypedDict, closed=True):
    resource_arn: NotRequired["capo_backup_gateway.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource from which you removed tags.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceOutput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceOutput:
    out: UntagResourceOutput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    return out
