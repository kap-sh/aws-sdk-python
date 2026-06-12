"""Generated from Smithy shape ``com.amazonaws.storagegateway#AssignTapePoolInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.boolean2
    import aws_sdk_storage_gateway.types.pool_id
    import aws_sdk_storage_gateway.types.tape_arn


class AssignTapePoolInput(TypedDict):
    tape_arn: "aws_sdk_storage_gateway.types.tape_arn.TapeARN"
    """<p>The unique Amazon Resource Name (ARN) of the virtual tape that you want to add to the tape pool.</p>"""
    pool_id: "aws_sdk_storage_gateway.types.pool_id.PoolId"
    """<p>The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.</p>"""
    bypass_governance_retention: "aws_sdk_storage_gateway.types.boolean2.Boolean2"
    """<p>Set permissions to bypass governance retention. If the lock type of the archived tape is <code>Governance</code>, the tape's archived age is not older than <code>RetentionLockInDays</code>, and the user does not already have <code>BypassGovernanceRetention</code>, setting this to TRUE enables the user to bypass the retention lock. This parameter is set to true by default for calls from the console.</p> <p>Valid values: <code>TRUE</code> | <code>FALSE</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssignTapePoolInput) -> dict:
    out: dict = {}
    out["TapeARN"] = value["tape_arn"]
    out["PoolId"] = value["pool_id"]
    out["BypassGovernanceRetention"] = value.get("bypass_governance_retention", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> AssignTapePoolInput:
    out: AssignTapePoolInput = {}  # type: ignore[typeddict-item]
    if "TapeARN" in data:
        out["tape_arn"] = data["TapeARN"]
    else:
        raise DeserializationError("AssignTapePoolInput.tape_arn required")
    if "PoolId" in data:
        out["pool_id"] = data["PoolId"]
    else:
        raise DeserializationError("AssignTapePoolInput.pool_id required")
    if "BypassGovernanceRetention" in data:
        out["bypass_governance_retention"] = data["BypassGovernanceRetention"]
    else:
        out["bypass_governance_retention"] = False
    return out
