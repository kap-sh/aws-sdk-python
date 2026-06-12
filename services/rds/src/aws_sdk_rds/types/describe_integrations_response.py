"""Generated from Smithy shape ``com.amazonaws.rds#DescribeIntegrationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.integration_list
    import aws_sdk_rds.types.marker


class DescribeIntegrationsResponse(TypedDict):
    marker: NotRequired["aws_sdk_rds.types.marker.Marker"]
    """<p>A pagination token that can be used in a later <code>DescribeIntegrations</code> request.</p>"""
    integrations: NotRequired["aws_sdk_rds.types.integration_list.IntegrationList"]
    """<p>A list of integrations.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeIntegrationsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "integrations" in value:
        import aws_sdk_rds.types.integration_list

        aws_sdk_rds.types.integration_list.serialize_query(
            value["integrations"], pairs, f"{prefix}.Integrations"
        )


def deserialize_query(el: Element) -> DescribeIntegrationsResponse:
    out: DescribeIntegrationsResponse = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_integrations = el.find("Integrations")
    if child_integrations is not None:
        import aws_sdk_rds.types.integration_list

        out["integrations"] = aws_sdk_rds.types.integration_list.deserialize_query(
            child_integrations
        )
    return out
