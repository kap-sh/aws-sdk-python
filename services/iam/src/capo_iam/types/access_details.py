"""Generated from Smithy shape ``com.amazonaws.iam#AccessDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.access_detail

AccessDetails: TypeAlias = list["capo_iam.types.access_detail.AccessDetail"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AccessDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.access_detail

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.access_detail.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AccessDetails:
    import capo_iam.types.access_detail

    out: AccessDetails = []
    for child in el.findall("member"):
        out.append(capo_iam.types.access_detail.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AccessDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.access_detail

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.access_detail.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> AccessDetails:
    import capo_iam.types.access_detail

    out: AccessDetails = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.access_detail.deserialize_query(child))
    return out
