"""Generated from Smithy shape ``com.amazonaws.cloudformation#ActivateOrganizationsAccessInput``."""

from typing_extensions import TypedDict

from aws_sdk_cloudformation._protocol.xml import Element


class ActivateOrganizationsAccessInput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: ActivateOrganizationsAccessInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> ActivateOrganizationsAccessInput:
    out: ActivateOrganizationsAccessInput = {}  # type: ignore[typeddict-item]
    return out
