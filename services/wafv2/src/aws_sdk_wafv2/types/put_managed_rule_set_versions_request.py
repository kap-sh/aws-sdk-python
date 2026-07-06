"""Generated from Smithy shape ``com.amazonaws.wafv2#PutManagedRuleSetVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.entity_id
    import aws_sdk_wafv2.types.entity_name
    import aws_sdk_wafv2.types.lock_token
    import aws_sdk_wafv2.types.scope
    import aws_sdk_wafv2.types.version_key_string
    import aws_sdk_wafv2.types.versions_to_publish


class PutManagedRuleSetVersionsRequest(TypedDict, closed=True):
    name: "aws_sdk_wafv2.types.entity_name.EntityName"
    """<p>The name of the managed rule set. You use this, along with the rule set ID, to identify the rule set.</p> <p>This name is assigned to the corresponding managed rule group, which your customers can access and use. </p>"""
    scope: "aws_sdk_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    id: "aws_sdk_wafv2.types.entity_id.EntityId"
    """<p>A unique identifier for the managed rule set. The ID is returned in the responses to commands like <code>list</code>. You provide it to operations like <code>get</code> and <code>update</code>.</p>"""
    lock_token: "aws_sdk_wafv2.types.lock_token.LockToken"
    """<p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>"""
    recommended_version: NotRequired[
        "aws_sdk_wafv2.types.version_key_string.VersionKeyString"
    ]
    """<p>The version of the named managed rule group that you'd like your customers to choose, from among your version offerings. </p>"""
    versions_to_publish: NotRequired[
        "aws_sdk_wafv2.types.versions_to_publish.VersionsToPublish"
    ]
    """<p>The versions of the named managed rule group that you want to offer to your customers. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutManagedRuleSetVersionsRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_wafv2.types.scope

    out["Scope"] = aws_sdk_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    out["Id"] = value["id"]
    out["LockToken"] = value["lock_token"]
    if "recommended_version" in value:
        out["RecommendedVersion"] = value["recommended_version"]
    if "versions_to_publish" in value:
        import aws_sdk_wafv2.types.versions_to_publish

        out["VersionsToPublish"] = (
            aws_sdk_wafv2.types.versions_to_publish.serialize_aws_json_1_1(
                value["versions_to_publish"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutManagedRuleSetVersionsRequest:
    out: PutManagedRuleSetVersionsRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PutManagedRuleSetVersionsRequest.name required")
    if "Scope" in data:
        import aws_sdk_wafv2.types.scope

        out["scope"] = aws_sdk_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        raise DeserializationError("PutManagedRuleSetVersionsRequest.scope required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("PutManagedRuleSetVersionsRequest.id required")
    if "LockToken" in data:
        out["lock_token"] = data["LockToken"]
    else:
        raise DeserializationError(
            "PutManagedRuleSetVersionsRequest.lock_token required"
        )
    if "RecommendedVersion" in data:
        out["recommended_version"] = data["RecommendedVersion"]
    if "VersionsToPublish" in data:
        import aws_sdk_wafv2.types.versions_to_publish

        out["versions_to_publish"] = (
            aws_sdk_wafv2.types.versions_to_publish.deserialize_aws_json_1_1(
                data["VersionsToPublish"]
            )
        )
    return out
