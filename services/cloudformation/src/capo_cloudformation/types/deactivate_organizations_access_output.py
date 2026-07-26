"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeactivateOrganizationsAccessOutput``."""

from typing_extensions import TypedDict

from capo_cloudformation._protocol.xml import Element


class DeactivateOrganizationsAccessOutput(TypedDict, closed=True):
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
