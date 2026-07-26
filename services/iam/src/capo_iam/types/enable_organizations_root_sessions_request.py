"""Generated from Smithy shape ``com.amazonaws.iam#EnableOrganizationsRootSessionsRequest``."""

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element


class EnableOrganizationsRootSessionsRequest(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: EnableOrganizationsRootSessionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> EnableOrganizationsRootSessionsRequest:
    out: EnableOrganizationsRootSessionsRequest = {}  # type: ignore[typeddict-item]
    return out
