"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#OpenTunnelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsecuretunneling.types.description
    import capo_iotsecuretunneling.types.destination_config
    import capo_iotsecuretunneling.types.tag_list
    import capo_iotsecuretunneling.types.timeout_config


class OpenTunnelRequest(TypedDict, closed=True):
    description: NotRequired["capo_iotsecuretunneling.types.description.Description"]
    """<p>A short text description of the tunnel. </p>"""
    tags: NotRequired["capo_iotsecuretunneling.types.tag_list.TagList"]
    """<p>A collection of tag metadata.</p>"""
    destination_config: NotRequired[
        "capo_iotsecuretunneling.types.destination_config.DestinationConfig"
    ]
    """<p>The destination configuration for the OpenTunnel request.</p>"""
    timeout_config: NotRequired[
        "capo_iotsecuretunneling.types.timeout_config.TimeoutConfig"
    ]
    """<p>Timeout configuration for a tunnel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenTunnelRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_iotsecuretunneling.types.tag_list

        out["tags"] = capo_iotsecuretunneling.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "destination_config" in value:
        import capo_iotsecuretunneling.types.destination_config

        out["destinationConfig"] = (
            capo_iotsecuretunneling.types.destination_config.serialize_aws_json_1_1(
                value["destination_config"]
            )
        )
    if "timeout_config" in value:
        import capo_iotsecuretunneling.types.timeout_config

        out["timeoutConfig"] = (
            capo_iotsecuretunneling.types.timeout_config.serialize_aws_json_1_1(
                value["timeout_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenTunnelRequest:
    out: OpenTunnelRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import capo_iotsecuretunneling.types.tag_list

        out["tags"] = capo_iotsecuretunneling.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "destinationConfig" in data:
        import capo_iotsecuretunneling.types.destination_config

        out["destination_config"] = (
            capo_iotsecuretunneling.types.destination_config.deserialize_aws_json_1_1(
                data["destinationConfig"]
            )
        )
    if "timeoutConfig" in data:
        import capo_iotsecuretunneling.types.timeout_config

        out["timeout_config"] = (
            capo_iotsecuretunneling.types.timeout_config.deserialize_aws_json_1_1(
                data["timeoutConfig"]
            )
        )
    return out
