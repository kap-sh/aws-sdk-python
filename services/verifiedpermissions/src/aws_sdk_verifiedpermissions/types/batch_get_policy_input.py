"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchGetPolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.batch_get_policy_input_list


class BatchGetPolicyInput(TypedDict):
    requests: "aws_sdk_verifiedpermissions.types.batch_get_policy_input_list.BatchGetPolicyInputList"
    """<p>An array of up to 100 policies you want information about.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetPolicyInput) -> dict:
    out: dict = {}
    import aws_sdk_verifiedpermissions.types.batch_get_policy_input_list

    out["requests"] = (
        aws_sdk_verifiedpermissions.types.batch_get_policy_input_list.serialize_aws_json_1_0(
            value["requests"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetPolicyInput:
    out: BatchGetPolicyInput = {}  # type: ignore[typeddict-item]
    if "requests" in data:
        import aws_sdk_verifiedpermissions.types.batch_get_policy_input_list

        out["requests"] = (
            aws_sdk_verifiedpermissions.types.batch_get_policy_input_list.deserialize_aws_json_1_0(
                data["requests"]
            )
        )
    else:
        raise DeserializationError("BatchGetPolicyInput.requests required")
    return out
