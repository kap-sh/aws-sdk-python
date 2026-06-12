"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeactivateOrganizationsAccessOutput``."""

from typing import TypedDict

from aws_sdk_cloudformation._protocol.xml import Element


class DeactivateOrganizationsAccessOutput(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeactivateOrganizationsAccessOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> DeactivateOrganizationsAccessOutput:
    out: DeactivateOrganizationsAccessOutput = {}  # type: ignore[typeddict-item]
    return out
