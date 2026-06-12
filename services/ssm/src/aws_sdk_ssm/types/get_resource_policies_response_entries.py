"""Generated from Smithy shape ``com.amazonaws.ssm#GetResourcePoliciesResponseEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.get_resource_policies_response_entry

GetResourcePoliciesResponseEntries: TypeAlias = list[
    "aws_sdk_ssm.types.get_resource_policies_response_entry.GetResourcePoliciesResponseEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePoliciesResponseEntries) -> list:
    import aws_sdk_ssm.types.get_resource_policies_response_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.get_resource_policies_response_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GetResourcePoliciesResponseEntries:
    import aws_sdk_ssm.types.get_resource_policies_response_entry

    out: GetResourcePoliciesResponseEntries = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.get_resource_policies_response_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
