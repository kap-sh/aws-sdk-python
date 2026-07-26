"""Generated from Smithy shape ``com.amazonaws.emr#LogTypeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.log_type
    import capo_emr.types.log_upload_policy_value

LogTypeMap: TypeAlias = dict[
    "capo_emr.types.log_type.LogType",
    "capo_emr.types.log_upload_policy_value.LogUploadPolicyValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: LogTypeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_emr.types.log_type
        import capo_emr.types.log_upload_policy_value

        out[capo_emr.types.log_type.serialize_aws_json_1_1(key)] = (
            capo_emr.types.log_upload_policy_value.serialize_aws_json_1_1(value)
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LogTypeMap:
    out: LogTypeMap = {}
    for key, value in data.items():
        import capo_emr.types.log_type
        import capo_emr.types.log_upload_policy_value

        out[capo_emr.types.log_type.deserialize_aws_json_1_1(key)] = (
            capo_emr.types.log_upload_policy_value.deserialize_aws_json_1_1(value)
        )
    return out
