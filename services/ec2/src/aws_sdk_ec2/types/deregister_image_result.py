"""Generated from Smithy shape ``com.amazonaws.ec2#DeregisterImageResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.delete_snapshot_result_set

DeregisterImageResult = TypedDict(
    "DeregisterImageResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.boolean.Boolean"],
        "delete_snapshot_results": NotRequired[
            "aws_sdk_ec2.types.delete_snapshot_result_set.DeleteSnapshotResultSet"
        ],
    },
)
