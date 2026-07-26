"""Generated from Smithy shape ``com.amazonaws.iot#GetPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.date_type
    import capo_iot.types.generation_id
    import capo_iot.types.policy_arn
    import capo_iot.types.policy_document
    import capo_iot.types.policy_name
    import capo_iot.types.policy_version_id


class GetPolicyResponse(TypedDict, closed=True):
    policy_name: NotRequired["capo_iot.types.policy_name.PolicyName"]
    """<p>The policy name.</p>"""
    policy_arn: NotRequired["capo_iot.types.policy_arn.PolicyArn"]
    """<p>The policy ARN.</p>"""
    policy_document: NotRequired["capo_iot.types.policy_document.PolicyDocument"]
    """<p>The JSON document that describes the policy.</p>"""
    default_version_id: NotRequired["capo_iot.types.policy_version_id.PolicyVersionId"]
    """<p>The default policy version ID.</p>"""
    creation_date: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The date the policy was created.</p>"""
    last_modified_date: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The date the policy was last modified.</p>"""
    generation_id: NotRequired["capo_iot.types.generation_id.GenerationId"]
    """<p>The generation ID of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyResponse) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "policy_document" in value:
        out["policyDocument"] = value["policy_document"]
    if "default_version_id" in value:
        out["defaultVersionId"] = value["default_version_id"]
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


def deserialize_json(data: dict) -> GetPolicyResponse:
    out: GetPolicyResponse = {}  # type: ignore[typeddict-item]
    if "policyName" in data:
        out["policy_name"] = data["policyName"]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    if "policyDocument" in data:
        out["policy_document"] = data["policyDocument"]
    if "defaultVersionId" in data:
        out["default_version_id"] = data["defaultVersionId"]
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
