"""Generated from Smithy shape ``com.amazonaws.ses#GetIdentityPoliciesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.policy_map


class GetIdentityPoliciesResponse(TypedDict):
    policies: "aws_sdk_ses.types.policy_map.PolicyMap"
    """<p>A map of policy names to policies.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetIdentityPoliciesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.policy_map

    aws_sdk_ses.types.policy_map.serialize_query(
        value["policies"], pairs, f"{prefix}.Policies"
    )


def deserialize_query(el: Element) -> GetIdentityPoliciesResponse:
    out: GetIdentityPoliciesResponse = {}  # type: ignore[typeddict-item]
    child_policies = el.find("Policies")
    if child_policies is not None:
        import aws_sdk_ses.types.policy_map

        out["policies"] = aws_sdk_ses.types.policy_map.deserialize_query(child_policies)
    else:
        raise DeserializationError("GetIdentityPoliciesResponse.policies required")
    return out
