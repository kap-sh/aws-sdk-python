"""Generated from Smithy shape ``com.amazonaws.cloudsearch#UpdateServiceAccessPoliciesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.access_policies_status


class UpdateServiceAccessPoliciesResponse(TypedDict):
    access_policies: (
        "aws_sdk_cloudsearch.types.access_policies_status.AccessPoliciesStatus"
    )
    """<p>The access rules configured for the domain.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateServiceAccessPoliciesResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_cloudsearch.types.access_policies_status

    aws_sdk_cloudsearch.types.access_policies_status.serialize_query(
        value["access_policies"], pairs, f"{prefix}.AccessPolicies"
    )


def deserialize_query(el: Element) -> UpdateServiceAccessPoliciesResponse:
    out: UpdateServiceAccessPoliciesResponse = {}  # type: ignore[typeddict-item]
    child_access_policies = el.find("AccessPolicies")
    if child_access_policies is not None:
        import aws_sdk_cloudsearch.types.access_policies_status

        out["access_policies"] = (
            aws_sdk_cloudsearch.types.access_policies_status.deserialize_query(
                child_access_policies
            )
        )
    else:
        raise DeserializationError(
            "UpdateServiceAccessPoliciesResponse.access_policies required"
        )
    return out
