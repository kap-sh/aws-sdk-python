"""Generated from Smithy shape ``com.amazonaws.iam#EnableOrganizationsRootCredentialsManagementRequest``."""

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element


class EnableOrganizationsRootCredentialsManagementRequest(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: EnableOrganizationsRootCredentialsManagementRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(
    el: Element,
) -> EnableOrganizationsRootCredentialsManagementRequest:
    out: EnableOrganizationsRootCredentialsManagementRequest = {}  # type: ignore[typeddict-item]
    return out
