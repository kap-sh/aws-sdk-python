"""Generated from Smithy shape ``com.amazonaws.iam#DisableOrganizationsRootCredentialsManagementRequest``."""

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element


class DisableOrganizationsRootCredentialsManagementRequest(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DisableOrganizationsRootCredentialsManagementRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(
    el: Element,
) -> DisableOrganizationsRootCredentialsManagementRequest:
    out: DisableOrganizationsRootCredentialsManagementRequest = {}  # type: ignore[typeddict-item]
    return out
