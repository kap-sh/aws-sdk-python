"""Generated from Smithy shape ``com.amazonaws.connect#UpdateRoutingProfileConcurrencyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.media_concurrencies
    import aws_sdk_connect.types.routing_profile_id


class UpdateRoutingProfileConcurrencyRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    routing_profile_id: "aws_sdk_connect.types.routing_profile_id.RoutingProfileId"
    """<p>The identifier of the routing profile.</p>"""
    media_concurrencies: "aws_sdk_connect.types.media_concurrencies.MediaConcurrencies"
    """<p>The channels that agents can handle in the Contact Control Panel (CCP).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoutingProfileConcurrencyRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.media_concurrencies

    out["MediaConcurrencies"] = (
        aws_sdk_connect.types.media_concurrencies.serialize_json(
            value["media_concurrencies"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateRoutingProfileConcurrencyRequest:
    out: UpdateRoutingProfileConcurrencyRequest = {}  # type: ignore[typeddict-item]
    if "MediaConcurrencies" in data:
        import aws_sdk_connect.types.media_concurrencies

        out["media_concurrencies"] = (
            aws_sdk_connect.types.media_concurrencies.deserialize_json(
                data["MediaConcurrencies"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRoutingProfileConcurrencyRequest.media_concurrencies required"
        )
    return out
