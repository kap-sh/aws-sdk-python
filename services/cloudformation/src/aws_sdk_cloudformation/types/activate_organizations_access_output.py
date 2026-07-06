"""Generated from Smithy shape ``com.amazonaws.cloudformation#ActivateOrganizationsAccessOutput``."""

from typing_extensions import TypedDict

from aws_sdk_cloudformation._protocol.xml import Element


class ActivateOrganizationsAccessOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: ActivateOrganizationsAccessOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> ActivateOrganizationsAccessOutput:
    out: ActivateOrganizationsAccessOutput = {}  # type: ignore[typeddict-item]
    return out
