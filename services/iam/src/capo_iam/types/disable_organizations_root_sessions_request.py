"""Generated from Smithy shape ``com.amazonaws.iam#DisableOrganizationsRootSessionsRequest``."""

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element


class DisableOrganizationsRootSessionsRequest(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DisableOrganizationsRootSessionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> DisableOrganizationsRootSessionsRequest:
    out: DisableOrganizationsRootSessionsRequest = {}  # type: ignore[typeddict-item]
    return out
