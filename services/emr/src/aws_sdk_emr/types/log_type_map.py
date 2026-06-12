"""Generated from Smithy shape ``com.amazonaws.emr#LogTypeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.log_type
    import aws_sdk_emr.types.log_upload_policy_value

LogTypeMap: TypeAlias = dict[
    "aws_sdk_emr.types.log_type.LogType",
    "aws_sdk_emr.types.log_upload_policy_value.LogUploadPolicyValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: LogTypeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_emr.types.log_type
        import aws_sdk_emr.types.log_upload_policy_value

        out[aws_sdk_emr.types.log_type.serialize_aws_json_1_1(key)] = (
            aws_sdk_emr.types.log_upload_policy_value.serialize_aws_json_1_1(value)
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LogTypeMap:
    out: LogTypeMap = {}
    for key, value in data.items():
        import aws_sdk_emr.types.log_type
        import aws_sdk_emr.types.log_upload_policy_value

        out[aws_sdk_emr.types.log_type.deserialize_aws_json_1_1(key)] = (
            aws_sdk_emr.types.log_upload_policy_value.deserialize_aws_json_1_1(value)
        )
    return out
