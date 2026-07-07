"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteTapeArchiveInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.boolean2
    import aws_sdk_storage_gateway.types.tape_arn


class DeleteTapeArchiveInput(TypedDict, closed=True):
    tape_arn: "aws_sdk_storage_gateway.types.tape_arn.TapeARN"
    """<p>The Amazon Resource Name (ARN) of the virtual tape to delete from the virtual tape shelf (VTS).</p>"""
    bypass_governance_retention: "aws_sdk_storage_gateway.types.boolean2.Boolean2"
    """<p>Set to <code>TRUE</code> to delete an archived tape that belongs to a custom pool with tape retention lock. Only archived tapes with tape retention lock set to <code>governance</code> can be deleted. Archived tapes with tape retention lock set to <code>compliance</code> can't be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTapeArchiveInput) -> dict:
    out: dict = {}
    out["TapeARN"] = value["tape_arn"]
    out["BypassGovernanceRetention"] = value.get("bypass_governance_retention", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTapeArchiveInput:
    out: DeleteTapeArchiveInput = {}  # type: ignore[typeddict-item]
    if "TapeARN" in data:
        out["tape_arn"] = data["TapeARN"]
    else:
        raise DeserializationError("DeleteTapeArchiveInput.tape_arn required")
    if "BypassGovernanceRetention" in data:
        out["bypass_governance_retention"] = data["BypassGovernanceRetention"]
    else:
        out["bypass_governance_retention"] = False
    return out
