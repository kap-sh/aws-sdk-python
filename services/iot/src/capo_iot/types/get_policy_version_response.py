"""Generated from Smithy shape ``com.amazonaws.iot#GetPolicyVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.date_type
    import capo_iot.types.generation_id
    import capo_iot.types.is_default_version
    import capo_iot.types.policy_arn
    import capo_iot.types.policy_document
    import capo_iot.types.policy_name
    import capo_iot.types.policy_version_id


class GetPolicyVersionResponse(TypedDict, closed=True):
    policy_arn: NotRequired["capo_iot.types.policy_arn.PolicyArn"]
    """<p>The policy ARN.</p>"""
    policy_name: NotRequired["capo_iot.types.policy_name.PolicyName"]
    """<p>The policy name.</p>"""
    policy_document: NotRequired["capo_iot.types.policy_document.PolicyDocument"]
    """<p>The JSON document that describes the policy.</p>"""
    policy_version_id: NotRequired["capo_iot.types.policy_version_id.PolicyVersionId"]
    """<p>The policy version ID.</p>"""
    is_default_version: "capo_iot.types.is_default_version.IsDefaultVersion"
    """<p>Specifies whether the policy version is the default.</p>"""
    creation_date: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The date the policy was created.</p>"""
    last_modified_date: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The date the policy was last modified.</p>"""
    generation_id: NotRequired["capo_iot.types.generation_id.GenerationId"]
    """<p>The generation ID of the policy version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyVersionResponse) -> dict:
    out: dict = {}
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "policy_document" in value:
        out["policyDocument"] = value["policy_document"]
    if "policy_version_id" in value:
        out["policyVersionId"] = value["policy_version_id"]
    out["isDefaultVersion"] = value.get("is_default_version", False)
    if "creation_date" in value:
        import capo_iot.types.date_type

        out["creationDate"] = capo_iot.types.date_type.serialize_json(
            value["creation_date"]
        )
    if "last_modified_date" in value:
        import capo_iot.types.date_type

        out["lastModifiedDate"] = capo_iot.types.date_type.serialize_json(
            value["last_modified_date"]
        )
    if "generation_id" in value:
        out["generationId"] = value["generation_id"]
    return out


def deserialize_json(data: dict) -> GetPolicyVersionResponse:
    out: GetPolicyVersionResponse = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    if "policyName" in data:
        out["policy_name"] = data["policyName"]
    if "policyDocument" in data:
        out["policy_document"] = data["policyDocument"]
    if "policyVersionId" in data:
        out["policy_version_id"] = data["policyVersionId"]
    if "isDefaultVersion" in data:
        out["is_default_version"] = data["isDefaultVersion"]
    else:
        out["is_default_version"] = False
    if "creationDate" in data:
        import capo_iot.types.date_type

        out["creation_date"] = capo_iot.types.date_type.deserialize_json(
            data["creationDate"]
        )
    if "lastModifiedDate" in data:
        import capo_iot.types.date_type

        out["last_modified_date"] = capo_iot.types.date_type.deserialize_json(
            data["lastModifiedDate"]
        )
    if "generationId" in data:
        out["generation_id"] = data["generationId"]
    return out
