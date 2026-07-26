"""Generated from Smithy shape ``com.amazonaws.iam#OpenIDConnectProviderListEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.arn_type


class OpenIDConnectProviderListEntry(TypedDict, closed=True):
    arn: NotRequired["capo_iam.types.arn_type.arnType"]


# --- awsQuery ser/de ---
def serialize_query(
    value: OpenIDConnectProviderListEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "arn" in value:
        pairs.append((f"{prefix}.Arn", str(value["arn"])))


def deserialize_query(el: Element) -> OpenIDConnectProviderListEntry:
    out: OpenIDConnectProviderListEntry = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out
