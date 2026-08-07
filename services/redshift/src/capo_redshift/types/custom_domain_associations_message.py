"""Generated from Smithy shape ``com.amazonaws.redshift#CustomDomainAssociationsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.association_list
    import capo_redshift.types.string


class CustomDomainAssociationsMessage(TypedDict, closed=True):
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>The marker for the custom domain association.</p>"""
    associations: NotRequired["capo_redshift.types.association_list.AssociationList"]
    """<p>The associations for the custom domain.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CustomDomainAssociationsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "associations" in value:
        import capo_redshift.types.association_list

        capo_redshift.types.association_list.serialize_query(
            value["associations"], pairs, f"{key_prefix}Associations"
        )


def deserialize_query(el: Element) -> CustomDomainAssociationsMessage:
    out: CustomDomainAssociationsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_associations = el.find("Associations")
    if child_associations is not None:
        import capo_redshift.types.association_list

        out["associations"] = capo_redshift.types.association_list.deserialize_query(
            child_associations
        )
    return out
