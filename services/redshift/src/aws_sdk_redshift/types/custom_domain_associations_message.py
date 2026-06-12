"""Generated from Smithy shape ``com.amazonaws.redshift#CustomDomainAssociationsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.association_list
    import aws_sdk_redshift.types.string


class CustomDomainAssociationsMessage(TypedDict):
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The marker for the custom domain association.</p>"""
    associations: NotRequired["aws_sdk_redshift.types.association_list.AssociationList"]
    """<p>The associations for the custom domain.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CustomDomainAssociationsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "associations" in value:
        import aws_sdk_redshift.types.association_list

        aws_sdk_redshift.types.association_list.serialize_query(
            value["associations"], pairs, f"{prefix}.Associations"
        )


def deserialize_query(el: Element) -> CustomDomainAssociationsMessage:
    out: CustomDomainAssociationsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_associations = el.find("Associations")
    if child_associations is not None:
        import aws_sdk_redshift.types.association_list

        out["associations"] = aws_sdk_redshift.types.association_list.deserialize_query(
            child_associations
        )
    return out
