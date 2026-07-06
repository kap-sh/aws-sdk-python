"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListAutomaticTapeCreationPoliciesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.automatic_tape_creation_policy_infos


class ListAutomaticTapeCreationPoliciesOutput(TypedDict, closed=True):
    automatic_tape_creation_policy_infos: NotRequired[
        "aws_sdk_storage_gateway.types.automatic_tape_creation_policy_infos.AutomaticTapeCreationPolicyInfos"
    ]
    """<p>Gets a listing of information about the gateway's automatic tape creation policies, including the automatic tape creation rules and the gateway that is using the policies.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAutomaticTapeCreationPoliciesOutput) -> dict:
    out: dict = {}
    if "automatic_tape_creation_policy_infos" in value:
        import aws_sdk_storage_gateway.types.automatic_tape_creation_policy_infos

        out["AutomaticTapeCreationPolicyInfos"] = (
            aws_sdk_storage_gateway.types.automatic_tape_creation_policy_infos.serialize_aws_json_1_1(
                value["automatic_tape_creation_policy_infos"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAutomaticTapeCreationPoliciesOutput:
    out: ListAutomaticTapeCreationPoliciesOutput = {}  # type: ignore[typeddict-item]
    if "AutomaticTapeCreationPolicyInfos" in data:
        import aws_sdk_storage_gateway.types.automatic_tape_creation_policy_infos

        out["automatic_tape_creation_policy_infos"] = (
            aws_sdk_storage_gateway.types.automatic_tape_creation_policy_infos.deserialize_aws_json_1_1(
                data["AutomaticTapeCreationPolicyInfos"]
            )
        )
    return out
