"""Generated from Smithy shape ``com.amazonaws.glue#DescribeInboundIntegrationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.inbound_integrations_list
    import capo_glue.types.string128


class DescribeInboundIntegrationsResponse(TypedDict, closed=True):
    inbound_integrations: NotRequired[
        "capo_glue.types.inbound_integrations_list.InboundIntegrationsList"
    ]
    """<p>A list of inbound integrations.</p>"""
    marker: NotRequired["capo_glue.types.string128.String128"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInboundIntegrationsResponse) -> dict:
    out: dict = {}
    if "inbound_integrations" in value:
        import capo_glue.types.inbound_integrations_list

        out["InboundIntegrations"] = (
            capo_glue.types.inbound_integrations_list.serialize_aws_json_1_1(
                value["inbound_integrations"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInboundIntegrationsResponse:
    out: DescribeInboundIntegrationsResponse = {}  # type: ignore[typeddict-item]
    if "InboundIntegrations" in data:
        import capo_glue.types.inbound_integrations_list

        out["inbound_integrations"] = (
            capo_glue.types.inbound_integrations_list.deserialize_aws_json_1_1(
                data["InboundIntegrations"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
