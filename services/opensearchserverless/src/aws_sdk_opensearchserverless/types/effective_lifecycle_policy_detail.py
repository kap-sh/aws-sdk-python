"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#EffectiveLifecyclePolicyDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.lifecycle_policy_type
    import aws_sdk_opensearchserverless.types.policy_name
    import aws_sdk_opensearchserverless.types.resource
    import aws_sdk_opensearchserverless.types.resource_type


class EffectiveLifecyclePolicyDetail(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType"
    ]
    """<p>The type of lifecycle policy.</p>"""
    resource: NotRequired["aws_sdk_opensearchserverless.types.resource.Resource"]
    """<p>The name of the OpenSearch Serverless index resource.</p>"""
    policy_name: NotRequired[
        "aws_sdk_opensearchserverless.types.policy_name.PolicyName"
    ]
    """<p>The name of the lifecycle policy.</p>"""
    resource_type: NotRequired[
        "aws_sdk_opensearchserverless.types.resource_type.ResourceType"
    ]
    """<p>The type of OpenSearch Serverless resource. Currently, the only supported resource is <code>index</code>.</p>"""
    retention_period: NotRequired["str"]
    """<p>The minimum number of index retention in days or hours. This is an optional parameter that will return only if it’s set.</p>"""
    no_min_retention_period: NotRequired["bool"]
    """<p>The minimum number of index retention days set. That is an optional param that will return as <code>true</code> if the minimum number of days or hours is not set to a index resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EffectiveLifecyclePolicyDetail) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "resource" in value:
        out["resource"] = value["resource"]
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "retention_period" in value:
        out["retentionPeriod"] = value["retention_period"]
    if "no_min_retention_period" in value:
        out["noMinRetentionPeriod"] = value["no_min_retention_period"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EffectiveLifecyclePolicyDetail:
    out: EffectiveLifecyclePolicyDetail = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "resource" in data:
        out["resource"] = data["resource"]
    if "policyName" in data:
        out["policy_name"] = data["policyName"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "retentionPeriod" in data:
        out["retention_period"] = data["retentionPeriod"]
    if "noMinRetentionPeriod" in data:
        out["no_min_retention_period"] = data["noMinRetentionPeriod"]
    return out
