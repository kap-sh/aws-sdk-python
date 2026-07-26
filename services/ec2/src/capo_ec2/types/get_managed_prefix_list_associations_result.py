"""Generated from Smithy shape ``com.amazonaws.ec2#GetManagedPrefixListAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.prefix_list_association_set
    import capo_ec2.types.string


class GetManagedPrefixListAssociationsResult(TypedDict, closed=True):
    prefix_list_associations: NotRequired[
        "capo_ec2.types.prefix_list_association_set.PrefixListAssociationSet"
    ]
    """<p>Information about the associations.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetManagedPrefixListAssociationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "prefix_list_associations" in value:
        import capo_ec2.types.prefix_list_association_set

        capo_ec2.types.prefix_list_association_set.serialize_ec2_query(
            value["prefix_list_associations"],
            pairs,
            f"{prefix}.PrefixListAssociationSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetManagedPrefixListAssociationsResult:
    out: GetManagedPrefixListAssociationsResult = {}  # type: ignore[typeddict-item]
    if el.find("PrefixListAssociationSet") is not None:
        import capo_ec2.types.prefix_list_association_set

        out["prefix_list_associations"] = (
            capo_ec2.types.prefix_list_association_set.deserialize_ec2_query(
                el, "PrefixListAssociationSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
