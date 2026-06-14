"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#IsAuthorizedWithTokenOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.decision
    import aws_sdk_verifiedpermissions.types.determining_policy_list
    import aws_sdk_verifiedpermissions.types.entity_identifier
    import aws_sdk_verifiedpermissions.types.evaluation_error_list


class IsAuthorizedWithTokenOutput(TypedDict):
    decision: "aws_sdk_verifiedpermissions.types.decision.Decision"
    """<p>An authorization decision that indicates if the authorization request should be allowed or denied.</p>"""
    determining_policies: "aws_sdk_verifiedpermissions.types.determining_policy_list.DeterminingPolicyList"
    """<p>The list of determining policies used to make the authorization decision. For example, if there are multiple matching policies, where at least one is a forbid policy, then because forbid always overrides permit the forbid policies are the determining policies. If all matching policies are permit policies, then those policies are the determining policies. When no policies match and the response is the default DENY, there are no determining policies.</p>"""
    errors: (
        "aws_sdk_verifiedpermissions.types.evaluation_error_list.EvaluationErrorList"
    )
    """<p>Errors that occurred while making an authorization decision. For example, a policy references an entity or entity attribute that does not exist in the slice.</p>"""
    principal: NotRequired[
        "aws_sdk_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>The identifier of the principal in the ID or access token.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IsAuthorizedWithTokenOutput) -> dict:
    out: dict = {}
    import aws_sdk_verifiedpermissions.types.decision

    out["decision"] = aws_sdk_verifiedpermissions.types.decision.serialize_aws_json_1_0(
        value["decision"]
    )
    import aws_sdk_verifiedpermissions.types.determining_policy_list

    out["determiningPolicies"] = (
        aws_sdk_verifiedpermissions.types.determining_policy_list.serialize_aws_json_1_0(
            value["determining_policies"]
        )
    )
    import aws_sdk_verifiedpermissions.types.evaluation_error_list

    out["errors"] = (
        aws_sdk_verifiedpermissions.types.evaluation_error_list.serialize_aws_json_1_0(
            value["errors"]
        )
    )
    if "principal" in value:
        import aws_sdk_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            aws_sdk_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["principal"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IsAuthorizedWithTokenOutput:
    out: IsAuthorizedWithTokenOutput = {}  # type: ignore[typeddict-item]
    if "decision" in data:
        import aws_sdk_verifiedpermissions.types.decision

        out["decision"] = (
            aws_sdk_verifiedpermissions.types.decision.deserialize_aws_json_1_0(
                data["decision"]
            )
        )
    else:
        raise DeserializationError("IsAuthorizedWithTokenOutput.decision required")
    if "determiningPolicies" in data:
        import aws_sdk_verifiedpermissions.types.determining_policy_list

        out["determining_policies"] = (
            aws_sdk_verifiedpermissions.types.determining_policy_list.deserialize_aws_json_1_0(
                data["determiningPolicies"]
            )
        )
    else:
        raise DeserializationError(
            "IsAuthorizedWithTokenOutput.determining_policies required"
        )
    if "errors" in data:
        import aws_sdk_verifiedpermissions.types.evaluation_error_list

        out["errors"] = (
            aws_sdk_verifiedpermissions.types.evaluation_error_list.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("IsAuthorizedWithTokenOutput.errors required")
    if "principal" in data:
        import aws_sdk_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            aws_sdk_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["principal"]
            )
        )
    return out
