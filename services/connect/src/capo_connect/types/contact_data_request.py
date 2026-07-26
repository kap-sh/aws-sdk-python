"""Generated from Smithy shape ``com.amazonaws.connect#ContactDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.attributes
    import capo_connect.types.campaign
    import capo_connect.types.endpoint
    import capo_connect.types.outbound_strategy
    import capo_connect.types.queue_id
    import capo_connect.types.request_identifier


class ContactDataRequest(TypedDict, closed=True):
    system_endpoint: NotRequired["capo_connect.types.endpoint.Endpoint"]
    """<p>Endpoint associated with the Connect Customer instance from which outbound contact will be initiated for the campaign.</p>"""
    customer_endpoint: NotRequired["capo_connect.types.endpoint.Endpoint"]
    """<p>Endpoint of the customer for which contact will be initiated.</p>"""
    request_identifier: NotRequired[
        "capo_connect.types.request_identifier.RequestIdentifier"
    ]
    """<p>Identifier to uniquely identify individual requests in the batch.</p>"""
    queue_id: NotRequired["capo_connect.types.queue_id.QueueId"]
    """<p>The identifier of the queue associated with the Connect Customer instance in which contacts that are created will be queued.</p>"""
    attributes: NotRequired["capo_connect.types.attributes.Attributes"]
    """<p>List of attributes to be stored in a contact.</p>"""
    campaign: NotRequired["capo_connect.types.campaign.Campaign"]
    """<p>Structure to store information associated with a campaign.</p>"""
    outbound_strategy: NotRequired[
        "capo_connect.types.outbound_strategy.OutboundStrategy"
    ]
    """<p>Information about the outbound strategy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactDataRequest) -> dict:
    out: dict = {}
    if "system_endpoint" in value:
        import capo_connect.types.endpoint

        out["SystemEndpoint"] = capo_connect.types.endpoint.serialize_json(
            value["system_endpoint"]
        )
    if "customer_endpoint" in value:
        import capo_connect.types.endpoint

        out["CustomerEndpoint"] = capo_connect.types.endpoint.serialize_json(
            value["customer_endpoint"]
        )
    if "request_identifier" in value:
        out["RequestIdentifier"] = value["request_identifier"]
    if "queue_id" in value:
        out["QueueId"] = value["queue_id"]
    if "attributes" in value:
        import capo_connect.types.attributes

        out["Attributes"] = capo_connect.types.attributes.serialize_json(
            value["attributes"]
        )
    if "campaign" in value:
        import capo_connect.types.campaign

        out["Campaign"] = capo_connect.types.campaign.serialize_json(value["campaign"])
    if "outbound_strategy" in value:
        import capo_connect.types.outbound_strategy

        out["OutboundStrategy"] = capo_connect.types.outbound_strategy.serialize_json(
            value["outbound_strategy"]
        )
    return out


def deserialize_json(data: dict) -> ContactDataRequest:
    out: ContactDataRequest = {}  # type: ignore[typeddict-item]
    if "SystemEndpoint" in data:
        import capo_connect.types.endpoint

        out["system_endpoint"] = capo_connect.types.endpoint.deserialize_json(
            data["SystemEndpoint"]
        )
    if "CustomerEndpoint" in data:
        import capo_connect.types.endpoint

        out["customer_endpoint"] = capo_connect.types.endpoint.deserialize_json(
            data["CustomerEndpoint"]
        )
    if "RequestIdentifier" in data:
        out["request_identifier"] = data["RequestIdentifier"]
    if "QueueId" in data:
        out["queue_id"] = data["QueueId"]
    if "Attributes" in data:
        import capo_connect.types.attributes

        out["attributes"] = capo_connect.types.attributes.deserialize_json(
            data["Attributes"]
        )
    if "Campaign" in data:
        import capo_connect.types.campaign

        out["campaign"] = capo_connect.types.campaign.deserialize_json(data["Campaign"])
    if "OutboundStrategy" in data:
        import capo_connect.types.outbound_strategy

        out["outbound_strategy"] = (
            capo_connect.types.outbound_strategy.deserialize_json(
                data["OutboundStrategy"]
            )
        )
    return out
