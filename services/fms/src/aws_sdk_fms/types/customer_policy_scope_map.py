"""Generated from Smithy shape ``com.amazonaws.fms#CustomerPolicyScopeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.customer_policy_scope_id_list
    import aws_sdk_fms.types.customer_policy_scope_id_type

CustomerPolicyScopeMap: TypeAlias = dict[
    "aws_sdk_fms.types.customer_policy_scope_id_type.CustomerPolicyScopeIdType",
    "aws_sdk_fms.types.customer_policy_scope_id_list.CustomerPolicyScopeIdList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: CustomerPolicyScopeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_fms.types.customer_policy_scope_id_list
        import aws_sdk_fms.types.customer_policy_scope_id_type

        out[
            aws_sdk_fms.types.customer_policy_scope_id_type.serialize_aws_json_1_1(key)
        ] = aws_sdk_fms.types.customer_policy_scope_id_list.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomerPolicyScopeMap:
    out: CustomerPolicyScopeMap = {}
    for key, value in data.items():
        import aws_sdk_fms.types.customer_policy_scope_id_list
        import aws_sdk_fms.types.customer_policy_scope_id_type

        out[
            aws_sdk_fms.types.customer_policy_scope_id_type.deserialize_aws_json_1_1(
                key
            )
        ] = aws_sdk_fms.types.customer_policy_scope_id_list.deserialize_aws_json_1_1(
            value
        )
    return out
