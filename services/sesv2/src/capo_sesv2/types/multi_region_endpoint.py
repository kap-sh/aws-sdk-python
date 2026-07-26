"""Generated from Smithy shape ``com.amazonaws.sesv2#MultiRegionEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.endpoint_id
    import capo_sesv2.types.endpoint_name
    import capo_sesv2.types.regions
    import capo_sesv2.types.status
    import capo_sesv2.types.timestamp


class MultiRegionEndpoint(TypedDict, closed=True):
    endpoint_name: NotRequired["capo_sesv2.types.endpoint_name.EndpointName"]
    """<p>The name of the multi-region endpoint (global-endpoint).</p>"""
    status: NotRequired["capo_sesv2.types.status.Status"]
    """<p>The status of the multi-region endpoint (global-endpoint).</p> <ul> <li> <p> <code>CREATING</code> – The resource is being provisioned.</p> </li> <li> <p> <code>READY</code> – The resource is ready to use.</p> </li> <li> <p> <code>FAILED</code> – The resource failed to be provisioned.</p> </li> <li> <p> <code>DELETING</code> – The resource is being deleted as requested.</p> </li> </ul>"""
    endpoint_id: NotRequired["capo_sesv2.types.endpoint_id.EndpointId"]
    """<p>The ID of the multi-region endpoint (global-endpoint).</p>"""
    regions: NotRequired["capo_sesv2.types.regions.Regions"]
    """<p>Primary and secondary regions between which multi-region endpoint splits sending traffic.</p>"""
    created_timestamp: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>The time stamp of when the multi-region endpoint (global-endpoint) was created.</p>"""
    last_updated_timestamp: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>The time stamp of when the multi-region endpoint (global-endpoint) was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiRegionEndpoint) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "status" in value:
        import capo_sesv2.types.status

        out["Status"] = capo_sesv2.types.status.serialize_json(value["status"])
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "regions" in value:
        import capo_sesv2.types.regions

        out["Regions"] = capo_sesv2.types.regions.serialize_json(value["regions"])
    if "created_timestamp" in value:
        import capo_sesv2.types.timestamp

        out["CreatedTimestamp"] = capo_sesv2.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "last_updated_timestamp" in value:
        import capo_sesv2.types.timestamp

        out["LastUpdatedTimestamp"] = capo_sesv2.types.timestamp.serialize_json(
            value["last_updated_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> MultiRegionEndpoint:
    out: MultiRegionEndpoint = {}  # type: ignore[typeddict-item]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    if "Status" in data:
        import capo_sesv2.types.status

        out["status"] = capo_sesv2.types.status.deserialize_json(data["Status"])
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    if "Regions" in data:
        import capo_sesv2.types.regions

        out["regions"] = capo_sesv2.types.regions.deserialize_json(data["Regions"])
    if "CreatedTimestamp" in data:
        import capo_sesv2.types.timestamp

        out["created_timestamp"] = capo_sesv2.types.timestamp.deserialize_json(
            data["CreatedTimestamp"]
        )
    if "LastUpdatedTimestamp" in data:
        import capo_sesv2.types.timestamp

        out["last_updated_timestamp"] = capo_sesv2.types.timestamp.deserialize_json(
            data["LastUpdatedTimestamp"]
        )
    return out
