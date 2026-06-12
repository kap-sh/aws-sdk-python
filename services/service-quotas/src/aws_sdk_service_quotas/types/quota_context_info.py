"""Generated from Smithy shape ``com.amazonaws.servicequotas#QuotaContextInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.quota_context_id
    import aws_sdk_service_quotas.types.quota_context_scope
    import aws_sdk_service_quotas.types.quota_context_scope_type


class QuotaContextInfo(TypedDict):
    context_scope: NotRequired[
        "aws_sdk_service_quotas.types.quota_context_scope.QuotaContextScope"
    ]
    """<p>Specifies the scope to which the quota value is applied. If the scope is <code>RESOURCE</code>, the quota value is applied to each resource in the Amazon Web Services account. If the scope is <code>ACCOUNT</code>, the quota value is applied to the Amazon Web Services account.</p>"""
    context_scope_type: NotRequired[
        "aws_sdk_service_quotas.types.quota_context_scope_type.QuotaContextScopeType"
    ]
    """<p>Specifies the resource type to which the quota can be applied.</p>"""
    context_id: NotRequired[
        "aws_sdk_service_quotas.types.quota_context_id.QuotaContextId"
    ]
    """<p>Specifies the resource, or resources, to which the quota applies. The value for this field is either an Amazon Resource Name (ARN) or *. If the value is an ARN, the quota value applies to that resource. If the value is *, then the quota value applies to all resources listed in the <code>ContextScopeType</code> field. The quota value applies to all resources for which you haven’t previously applied a quota value, and any new resources you create in your Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuotaContextInfo) -> dict:
    out: dict = {}
    if "context_scope" in value:
        import aws_sdk_service_quotas.types.quota_context_scope

        out["ContextScope"] = (
            aws_sdk_service_quotas.types.quota_context_scope.serialize_aws_json_1_1(
                value["context_scope"]
            )
        )
    if "context_scope_type" in value:
        out["ContextScopeType"] = value["context_scope_type"]
    if "context_id" in value:
        out["ContextId"] = value["context_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QuotaContextInfo:
    out: QuotaContextInfo = {}  # type: ignore[typeddict-item]
    if "ContextScope" in data:
        import aws_sdk_service_quotas.types.quota_context_scope

        out["context_scope"] = (
            aws_sdk_service_quotas.types.quota_context_scope.deserialize_aws_json_1_1(
                data["ContextScope"]
            )
        )
    if "ContextScopeType" in data:
        out["context_scope_type"] = data["ContextScopeType"]
    if "ContextId" in data:
        out["context_id"] = data["ContextId"]
    return out
