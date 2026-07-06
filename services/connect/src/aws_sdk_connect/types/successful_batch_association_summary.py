"""Generated from Smithy shape ``com.amazonaws.connect#SuccessfulBatchAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn


class SuccessfulBatchAssociationSummary(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the resource that was successfully associated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulBatchAssociationSummary) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> SuccessfulBatchAssociationSummary:
    out: SuccessfulBatchAssociationSummary = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    return out
