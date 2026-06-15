"""Generated from Smithy shape ``com.amazonaws.iam#ListPoliciesGrantingServiceAccessEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.policy_granting_service_access_list_type
    import aws_sdk_iam.types.service_namespace_type


class ListPoliciesGrantingServiceAccessEntry(TypedDict):
    service_namespace: NotRequired[
        "aws_sdk_iam.types.service_namespace_type.serviceNamespaceType"
    ]
    r"""<p>The namespace of the service that was accessed.</p> <p>To learn the service namespace of a service, see <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html\">Actions, resources, and condition keys for Amazon Web Services services</a> in the <i>Service Authorization Reference</i>. Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, <code>(service prefix: a4b)</code>. For more information about service namespaces, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces\">Amazon Web Services service namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    policies: NotRequired[
        "aws_sdk_iam.types.policy_granting_service_access_list_type.policyGrantingServiceAccessListType"
    ]
    """<p>The <code>PoliciesGrantingServiceAccess</code> object that contains details about the policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListPoliciesGrantingServiceAccessEntry,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "service_namespace" in value:
        pairs.append((f"{prefix}.ServiceNamespace", str(value["service_namespace"])))
    if "policies" in value:
        import aws_sdk_iam.types.policy_granting_service_access_list_type

        aws_sdk_iam.types.policy_granting_service_access_list_type.serialize_query(
            value["policies"], pairs, f"{prefix}.Policies"
        )


def deserialize_query(el: Element) -> ListPoliciesGrantingServiceAccessEntry:
    out: ListPoliciesGrantingServiceAccessEntry = {}  # type: ignore[typeddict-item]
    child_service_namespace = el.find("ServiceNamespace")
    if child_service_namespace is not None:
        out["service_namespace"] = str(child_service_namespace.text or "")
    child_policies = el.find("Policies")
    if child_policies is not None:
        import aws_sdk_iam.types.policy_granting_service_access_list_type

        out["policies"] = (
            aws_sdk_iam.types.policy_granting_service_access_list_type.deserialize_query(
                child_policies
            )
        )
    return out
