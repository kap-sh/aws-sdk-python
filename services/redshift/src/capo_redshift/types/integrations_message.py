"""Generated from Smithy shape ``com.amazonaws.redshift#IntegrationsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.integration_list
    import capo_redshift.types.string


class IntegrationsMessage(TypedDict, closed=True):
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request.</p>"""
    integrations: NotRequired["capo_redshift.types.integration_list.IntegrationList"]
    """<p>List of integrations that are described.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: IntegrationsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "integrations" in value:
        import capo_redshift.types.integration_list

        capo_redshift.types.integration_list.serialize_query(
            value["integrations"], pairs, f"{prefix}.Integrations"
        )


def deserialize_query(el: Element) -> IntegrationsMessage:
    out: IntegrationsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_integrations = el.find("Integrations")
    if child_integrations is not None:
        import capo_redshift.types.integration_list

        out["integrations"] = capo_redshift.types.integration_list.deserialize_query(
            child_integrations
        )
    return out
