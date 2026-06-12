"""Generated from Smithy shape ``com.amazonaws.networkmonitor#CreateProbeInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_networkmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmonitor.types.probe_input
    import aws_sdk_networkmonitor.types.resource_name
    import aws_sdk_networkmonitor.types.tag_map


class CreateProbeInput(TypedDict):
    monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor to associated with the probe. </p>"""
    probe: "aws_sdk_networkmonitor.types.probe_input.ProbeInput"
    """<p>Describes the details of an individual probe for a monitor.</p>"""
    client_token: NotRequired["str"]
    """<p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>"""
    tags: NotRequired["aws_sdk_networkmonitor.types.tag_map.TagMap"]
    """<p>The list of key-value pairs created and assigned to the probe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProbeInput) -> dict:
    out: dict = {}
    import aws_sdk_networkmonitor.types.probe_input

    out["probe"] = aws_sdk_networkmonitor.types.probe_input.serialize_json(
        value["probe"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_networkmonitor.types.tag_map

        out["tags"] = aws_sdk_networkmonitor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateProbeInput:
    out: CreateProbeInput = {}  # type: ignore[typeddict-item]
    if "probe" in data:
        import aws_sdk_networkmonitor.types.probe_input

        out["probe"] = aws_sdk_networkmonitor.types.probe_input.deserialize_json(
            data["probe"]
        )
    else:
        raise DeserializationError("CreateProbeInput.probe required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_networkmonitor.types.tag_map

        out["tags"] = aws_sdk_networkmonitor.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
