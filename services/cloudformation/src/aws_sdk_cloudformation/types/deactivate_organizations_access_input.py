"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeactivateOrganizationsAccessInput``."""

from typing_extensions import TypedDict

from aws_sdk_cloudformation._protocol.xml import Element


class DeactivateOrganizationsAccessInput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeactivateOrganizationsAccessInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeactivateOrganizationsAccessInput:
    out: DeactivateOrganizationsAccessInput = {}  # type: ignore[typeddict-item]
    return out
