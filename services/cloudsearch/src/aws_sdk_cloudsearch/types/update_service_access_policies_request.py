"""Generated from Smithy shape ``com.amazonaws.cloudsearch#UpdateServiceAccessPoliciesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.domain_name
    import aws_sdk_cloudsearch.types.policy_document


class UpdateServiceAccessPoliciesRequest(TypedDict):
    domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName"
    access_policies: "aws_sdk_cloudsearch.types.policy_document.PolicyDocument"
    """<p>The access rules you want to configure. These rules replace any existing rules. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateServiceAccessPoliciesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.DomainName", str(value["domain_name"])))
    pairs.append((f"{prefix}.AccessPolicies", str(value["access_policies"])))


def deserialize_query(el: Element) -> UpdateServiceAccessPoliciesRequest:
    out: UpdateServiceAccessPoliciesRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError(
            "UpdateServiceAccessPoliciesRequest.domain_name required"
        )
    child_access_policies = el.find("AccessPolicies")
    if child_access_policies is not None:
        out["access_policies"] = str(child_access_policies.text or "")
    else:
        raise DeserializationError(
            "UpdateServiceAccessPoliciesRequest.access_policies required"
        )
    return out
