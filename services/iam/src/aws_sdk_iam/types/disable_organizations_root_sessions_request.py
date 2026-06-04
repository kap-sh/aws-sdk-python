"""Generated from Smithy shape ``com.amazonaws.iam#DisableOrganizationsRootSessionsRequest``."""

from typing import TypedDict
from aws_sdk_iam._protocol.xml import Element


class DisableOrganizationsRootSessionsRequest(TypedDict):
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
