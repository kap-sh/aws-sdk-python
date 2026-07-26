"""Generated from Smithy shape ``com.amazonaws.iam#ListOrganizationsFeaturesRequest``."""

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element


class ListOrganizationsFeaturesRequest(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: ListOrganizationsFeaturesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> ListOrganizationsFeaturesRequest:
    out: ListOrganizationsFeaturesRequest = {}  # type: ignore[typeddict-item]
    return out
