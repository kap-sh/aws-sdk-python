"""Generated from Smithy shape ``com.amazonaws.redshift#AuthorizedAudienceList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string

AuthorizedAudienceList: TypeAlias = list["capo_redshift.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthorizedAudienceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> AuthorizedAudienceList:
    out: AuthorizedAudienceList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: AuthorizedAudienceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> AuthorizedAudienceList:
    out: AuthorizedAudienceList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
