"""Generated from Smithy shape ``com.amazonaws.sesv2#MultiRegionEndpoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.endpoint_id
    import aws_sdk_sesv2.types.endpoint_name
    import aws_sdk_sesv2.types.regions
    import aws_sdk_sesv2.types.status
    import aws_sdk_sesv2.types.timestamp


class MultiRegionEndpoint(TypedDict):
    endpoint_name: NotRequired["aws_sdk_sesv2.types.endpoint_name.EndpointName"]
    """<p>The name of the multi-region endpoint (global-endpoint).</p>"""
    status: NotRequired["aws_sdk_sesv2.types.status.Status"]
    """<p>The status of the multi-region endpoint (global-endpoint).</p> <ul> <li> <p> <code>CREATING</code> – The resource is being provisioned.</p> </li> <li> <p> <code>READY</code> – The resource is ready to use.</p> </li> <li> <p> <code>FAILED</code> – The resource failed to be provisioned.</p> </li> <li> <p> <code>DELETING</code> – The resource is being deleted as requested.</p> </li> </ul>"""
    endpoint_id: NotRequired["aws_sdk_sesv2.types.endpoint_id.EndpointId"]
    """<p>The ID of the multi-region endpoint (global-endpoint).</p>"""
    regions: NotRequired["aws_sdk_sesv2.types.regions.Regions"]
    """<p>Primary and secondary regions between which multi-region endpoint splits sending traffic.</p>"""
    created_timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>The time stamp of when the multi-region endpoint (global-endpoint) was created.</p>"""
    last_updated_timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>The time stamp of when the multi-region endpoint (global-endpoint) was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiRegionEndpoint) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "status" in value:
        import aws_sdk_sesv2.types.status

        out["Status"] = aws_sdk_sesv2.types.status.serialize_json(value["status"])
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "regions" in value:
        import aws_sdk_sesv2.types.regions

        out["Regions"] = aws_sdk_sesv2.types.regions.serialize_json(value["regions"])
    if "created_timestamp" in value:
        import aws_sdk_sesv2.types.timestamp

        out["CreatedTimestamp"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "last_updated_timestamp" in value:
        import aws_sdk_sesv2.types.timestamp

        out["LastUpdatedTimestamp"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["last_updated_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> MultiRegionEndpoint:
    out: MultiRegionEndpoint = {}  # type: ignore[typeddict-item]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    if "Status" in data:
        import aws_sdk_sesv2.types.status

        out["status"] = aws_sdk_sesv2.types.status.deserialize_json(data["Status"])
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    if "Regions" in data:
        import aws_sdk_sesv2.types.regions

        out["regions"] = aws_sdk_sesv2.types.regions.deserialize_json(data["Regions"])
    if "CreatedTimestamp" in data:
        import aws_sdk_sesv2.types.timestamp

        out["created_timestamp"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["CreatedTimestamp"]
        )
    if "LastUpdatedTimestamp" in data:
        import aws_sdk_sesv2.types.timestamp

        out["last_updated_timestamp"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["LastUpdatedTimestamp"]
        )
    return out
