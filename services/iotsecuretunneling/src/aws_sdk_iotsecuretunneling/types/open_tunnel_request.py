"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#OpenTunnelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsecuretunneling.types.description
    import aws_sdk_iotsecuretunneling.types.destination_config
    import aws_sdk_iotsecuretunneling.types.tag_list
    import aws_sdk_iotsecuretunneling.types.timeout_config


class OpenTunnelRequest(TypedDict, closed=True):
    description: NotRequired["aws_sdk_iotsecuretunneling.types.description.Description"]
    """<p>A short text description of the tunnel. </p>"""
    tags: NotRequired["aws_sdk_iotsecuretunneling.types.tag_list.TagList"]
    """<p>A collection of tag metadata.</p>"""
    destination_config: NotRequired[
        "aws_sdk_iotsecuretunneling.types.destination_config.DestinationConfig"
    ]
    """<p>The destination configuration for the OpenTunnel request.</p>"""
    timeout_config: NotRequired[
        "aws_sdk_iotsecuretunneling.types.timeout_config.TimeoutConfig"
    ]
    """<p>Timeout configuration for a tunnel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenTunnelRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_iotsecuretunneling.types.tag_list

        out["tags"] = aws_sdk_iotsecuretunneling.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "destination_config" in value:
        import aws_sdk_iotsecuretunneling.types.destination_config

        out["destinationConfig"] = (
            aws_sdk_iotsecuretunneling.types.destination_config.serialize_aws_json_1_1(
                value["destination_config"]
            )
        )
    if "timeout_config" in value:
        import aws_sdk_iotsecuretunneling.types.timeout_config

        out["timeoutConfig"] = (
            aws_sdk_iotsecuretunneling.types.timeout_config.serialize_aws_json_1_1(
                value["timeout_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenTunnelRequest:
    out: OpenTunnelRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_iotsecuretunneling.types.tag_list

        out["tags"] = (
            aws_sdk_iotsecuretunneling.types.tag_list.deserialize_aws_json_1_1(
                data["tags"]
            )
        )
    if "destinationConfig" in data:
        import aws_sdk_iotsecuretunneling.types.destination_config

        out["destination_config"] = (
            aws_sdk_iotsecuretunneling.types.destination_config.deserialize_aws_json_1_1(
                data["destinationConfig"]
            )
        )
    if "timeoutConfig" in data:
        import aws_sdk_iotsecuretunneling.types.timeout_config

        out["timeout_config"] = (
            aws_sdk_iotsecuretunneling.types.timeout_config.deserialize_aws_json_1_1(
                data["timeoutConfig"]
            )
        )
    return out
