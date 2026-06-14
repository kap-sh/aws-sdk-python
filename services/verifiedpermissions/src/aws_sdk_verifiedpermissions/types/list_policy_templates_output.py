"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ListPolicyTemplatesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.next_token
    import aws_sdk_verifiedpermissions.types.policy_templates_list


class ListPolicyTemplatesOutput(TypedDict):
    next_token: NotRequired["aws_sdk_verifiedpermissions.types.next_token.NextToken"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""
    policy_templates: (
        "aws_sdk_verifiedpermissions.types.policy_templates_list.PolicyTemplatesList"
    )
    """<p>The list of the policy templates in the specified policy store.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPolicyTemplatesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_verifiedpermissions.types.policy_templates_list

    out["policyTemplates"] = (
        aws_sdk_verifiedpermissions.types.policy_templates_list.serialize_aws_json_1_0(
            value["policy_templates"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPolicyTemplatesOutput:
    out: ListPolicyTemplatesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "policyTemplates" in data:
        import aws_sdk_verifiedpermissions.types.policy_templates_list

        out["policy_templates"] = (
            aws_sdk_verifiedpermissions.types.policy_templates_list.deserialize_aws_json_1_0(
                data["policyTemplates"]
            )
        )
    else:
        raise DeserializationError(
            "ListPolicyTemplatesOutput.policy_templates required"
        )
    return out
