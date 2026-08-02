"""Generated from Smithy shape ``com.amazonaws.rds#DescribeIntegrationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.integration_list
    import capo_rds.types.marker


class DescribeIntegrationsResponse(TypedDict, closed=True):
    marker: NotRequired["capo_rds.types.marker.Marker"]
    """<p>A pagination token that can be used in a later <code>DescribeIntegrations</code> request.</p>"""
    integrations: NotRequired["capo_rds.types.integration_list.IntegrationList"]
    """<p>A list of integrations.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeIntegrationsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "integrations" in value:
        import capo_rds.types.integration_list

        capo_rds.types.integration_list.serialize_query(
            value["integrations"], pairs, f"{key_prefix}Integrations"
        )


def deserialize_query(el: Element) -> DescribeIntegrationsResponse:
    out: DescribeIntegrationsResponse = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_integrations = el.find("Integrations")
    if child_integrations is not None:
        import capo_rds.types.integration_list

        out["integrations"] = capo_rds.types.integration_list.deserialize_query(
            child_integrations
        )
    return out
