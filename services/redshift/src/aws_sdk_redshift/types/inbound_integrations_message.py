"""Generated from Smithy shape ``com.amazonaws.redshift#InboundIntegrationsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.inbound_integration_list
    import aws_sdk_redshift.types.string


class InboundIntegrationsMessage(TypedDict):
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""
    inbound_integrations: NotRequired[
        "aws_sdk_redshift.types.inbound_integration_list.InboundIntegrationList"
    ]
    """<p>A list of <a>InboundIntegration</a> instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InboundIntegrationsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "inbound_integrations" in value:
        import aws_sdk_redshift.types.inbound_integration_list

        aws_sdk_redshift.types.inbound_integration_list.serialize_query(
            value["inbound_integrations"], pairs, f"{prefix}.InboundIntegrations"
        )


def deserialize_query(el: Element) -> InboundIntegrationsMessage:
    out: InboundIntegrationsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_inbound_integrations = el.find("InboundIntegrations")
    if child_inbound_integrations is not None:
        import aws_sdk_redshift.types.inbound_integration_list

        out["inbound_integrations"] = (
            aws_sdk_redshift.types.inbound_integration_list.deserialize_query(
                child_inbound_integrations
            )
        )
    return out
