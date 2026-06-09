"""Generated from Smithy shape ``com.amazonaws.iam#EnableOrganizationsRootSessionsRequest``."""

from typing import TypedDict

from aws_sdk_iam._protocol.xml import Element


class EnableOrganizationsRootSessionsRequest(TypedDict):
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
