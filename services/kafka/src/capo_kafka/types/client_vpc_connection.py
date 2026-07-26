"""Generated from Smithy shape ``com.amazonaws.kafka#ClientVpcConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.__timestamp_iso8601
    import capo_kafka.types.vpc_connection_state


class ClientVpcConnection(TypedDict, closed=True):
    authentication: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Information about the auth scheme of Vpc Connection.</p>"""
    creation_time: NotRequired[
        "capo_kafka.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>Creation time of the Vpc Connection.</p>"""
    state: NotRequired["capo_kafka.types.vpc_connection_state.VpcConnectionState"]
    """<p>State of the Vpc Connection.</p>"""
    vpc_connection_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The ARN that identifies the Vpc Connection.</p>"""
    owner: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Owner of the Vpc Connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientVpcConnection) -> dict:
    out: dict = {}
    if "authentication" in value:
        out["authentication"] = value["authentication"]
    if "creation_time" in value:
        import capo_kafka.types.__timestamp_iso8601

        out["creationTime"] = capo_kafka.types.__timestamp_iso8601.serialize_json(
            value["creation_time"]
        )
    if "state" in value:
        import capo_kafka.types.vpc_connection_state

        out["state"] = capo_kafka.types.vpc_connection_state.serialize_json(
            value["state"]
        )
    if "vpc_connection_arn" in value:
        out["vpcConnectionArn"] = value["vpc_connection_arn"]
    if "owner" in value:
        out["owner"] = value["owner"]
    return out


def deserialize_json(data: dict) -> ClientVpcConnection:
    out: ClientVpcConnection = {}  # type: ignore[typeddict-item]
    if "authentication" in data:
        out["authentication"] = data["authentication"]
    if "creationTime" in data:
        import capo_kafka.types.__timestamp_iso8601

        out["creation_time"] = capo_kafka.types.__timestamp_iso8601.deserialize_json(
            data["creationTime"]
        )
    if "state" in data:
        import capo_kafka.types.vpc_connection_state

        out["state"] = capo_kafka.types.vpc_connection_state.deserialize_json(
            data["state"]
        )
    if "vpcConnectionArn" in data:
        out["vpc_connection_arn"] = data["vpcConnectionArn"]
    if "owner" in data:
        out["owner"] = data["owner"]
    return out
