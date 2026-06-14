"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchGetPolicyOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.batch_get_policy_error_list
    import aws_sdk_verifiedpermissions.types.batch_get_policy_output_list


class BatchGetPolicyOutput(TypedDict):
    results: "aws_sdk_verifiedpermissions.types.batch_get_policy_output_list.BatchGetPolicyOutputList"
    """<p>Information about the policies listed in the request that were successfully returned. These results are returned in the order they were requested.</p>"""
    errors: "aws_sdk_verifiedpermissions.types.batch_get_policy_error_list.BatchGetPolicyErrorList"
    """<p>Information about the policies from the request that resulted in an error. These results are returned in the order they were requested.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetPolicyOutput) -> dict:
    out: dict = {}
    import aws_sdk_verifiedpermissions.types.batch_get_policy_output_list

    out["results"] = (
        aws_sdk_verifiedpermissions.types.batch_get_policy_output_list.serialize_aws_json_1_0(
            value["results"]
        )
    )
    import aws_sdk_verifiedpermissions.types.batch_get_policy_error_list

    out["errors"] = (
        aws_sdk_verifiedpermissions.types.batch_get_policy_error_list.serialize_aws_json_1_0(
            value["errors"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetPolicyOutput:
    out: BatchGetPolicyOutput = {}  # type: ignore[typeddict-item]
    if "results" in data:
        import aws_sdk_verifiedpermissions.types.batch_get_policy_output_list

        out["results"] = (
            aws_sdk_verifiedpermissions.types.batch_get_policy_output_list.deserialize_aws_json_1_0(
                data["results"]
            )
        )
    else:
        raise DeserializationError("BatchGetPolicyOutput.results required")
    if "errors" in data:
        import aws_sdk_verifiedpermissions.types.batch_get_policy_error_list

        out["errors"] = (
            aws_sdk_verifiedpermissions.types.batch_get_policy_error_list.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchGetPolicyOutput.errors required")
    return out
