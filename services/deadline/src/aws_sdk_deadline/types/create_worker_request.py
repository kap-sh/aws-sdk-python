"""Generated from Smithy shape ``com.amazonaws.deadline#CreateWorkerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.host_properties_request
    import aws_sdk_deadline.types.tags


class CreateWorkerRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm to connect to the worker.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID to connect to the worker.</p>"""
    host_properties: NotRequired[
        "aws_sdk_deadline.types.host_properties_request.HostPropertiesRequest"
    ]
    """<p>The IP address and host name of the worker.</p>"""
    client_token: NotRequired["aws_sdk_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    tags: NotRequired["aws_sdk_deadline.types.tags.Tags"]
    """<p>Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkerRequest) -> dict:
    out: dict = {}
    if "host_properties" in value:
        import aws_sdk_deadline.types.host_properties_request

        out["hostProperties"] = (
            aws_sdk_deadline.types.host_properties_request.serialize_json(
                value["host_properties"]
            )
        )
    if "tags" in value:
        import aws_sdk_deadline.types.tags

        out["tags"] = aws_sdk_deadline.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateWorkerRequest:
    out: CreateWorkerRequest = {}  # type: ignore[typeddict-item]
    if "hostProperties" in data:
        import aws_sdk_deadline.types.host_properties_request

        out["host_properties"] = (
            aws_sdk_deadline.types.host_properties_request.deserialize_json(
                data["hostProperties"]
            )
        )
    if "tags" in data:
        import aws_sdk_deadline.types.tags

        out["tags"] = aws_sdk_deadline.types.tags.deserialize_json(data["tags"])
    return out
