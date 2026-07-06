"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceConnector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.boolean
    import aws_sdk_chime_sdk_voice.types.iso8601_timestamp
    import aws_sdk_chime_sdk_voice.types.network_type
    import aws_sdk_chime_sdk_voice.types.non_empty_string
    import aws_sdk_chime_sdk_voice.types.string
    import aws_sdk_chime_sdk_voice.types.voice_connector_aws_region
    import aws_sdk_chime_sdk_voice.types.voice_connector_integration_type
    import aws_sdk_chime_sdk_voice.types.voice_connector_name


class VoiceConnector(TypedDict, closed=True):
    voice_connector_id: NotRequired[
        "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Voice Connector's ID.</p>"""
    aws_region: NotRequired[
        "aws_sdk_chime_sdk_voice.types.voice_connector_aws_region.VoiceConnectorAwsRegion"
    ]
    """<p>The AWS Region in which the Voice Connector is created. Default: us-east-1.</p>"""
    name: NotRequired[
        "aws_sdk_chime_sdk_voice.types.voice_connector_name.VoiceConnectorName"
    ]
    """<p>The Voice Connector's name.</p>"""
    outbound_host_name: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]
    """<p>The outbound host name for the Voice Connector.</p>"""
    require_encryption: NotRequired["aws_sdk_chime_sdk_voice.types.boolean.Boolean"]
    """<p>Enables or disables encryption for the Voice Connector.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The Voice Connector's creation timestamp, in ISO 8601 format.</p>"""
    updated_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The Voice Connector's updated timestamp, in ISO 8601 format.</p>"""
    voice_connector_arn: NotRequired[
        "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the Voice Connector.</p>"""
    integration_type: NotRequired[
        "aws_sdk_chime_sdk_voice.types.voice_connector_integration_type.VoiceConnectorIntegrationType"
    ]
    """<p>The connectors for use with Connect Customer.</p>"""
    network_type: NotRequired["aws_sdk_chime_sdk_voice.types.network_type.NetworkType"]
    """<p>The type of network of the Voice Connector. Either IPv4 only or dual-stack (IPv4 and IPv6).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceConnector) -> dict:
    out: dict = {}
    if "voice_connector_id" in value:
        out["VoiceConnectorId"] = value["voice_connector_id"]
    if "aws_region" in value:
        import aws_sdk_chime_sdk_voice.types.voice_connector_aws_region

        out["AwsRegion"] = (
            aws_sdk_chime_sdk_voice.types.voice_connector_aws_region.serialize_json(
                value["aws_region"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "outbound_host_name" in value:
        out["OutboundHostName"] = value["outbound_host_name"]
    if "require_encryption" in value:
        out["RequireEncryption"] = value["require_encryption"]
    if "created_timestamp" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    if "voice_connector_arn" in value:
        out["VoiceConnectorArn"] = value["voice_connector_arn"]
    if "integration_type" in value:
        import aws_sdk_chime_sdk_voice.types.voice_connector_integration_type

        out["IntegrationType"] = (
            aws_sdk_chime_sdk_voice.types.voice_connector_integration_type.serialize_json(
                value["integration_type"]
            )
        )
    if "network_type" in value:
        import aws_sdk_chime_sdk_voice.types.network_type

        out["NetworkType"] = aws_sdk_chime_sdk_voice.types.network_type.serialize_json(
            value["network_type"]
        )
    return out


def deserialize_json(data: dict) -> VoiceConnector:
    out: VoiceConnector = {}  # type: ignore[typeddict-item]
    if "VoiceConnectorId" in data:
        out["voice_connector_id"] = data["VoiceConnectorId"]
    if "AwsRegion" in data:
        import aws_sdk_chime_sdk_voice.types.voice_connector_aws_region

        out["aws_region"] = (
            aws_sdk_chime_sdk_voice.types.voice_connector_aws_region.deserialize_json(
                data["AwsRegion"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "OutboundHostName" in data:
        out["outbound_host_name"] = data["OutboundHostName"]
    if "RequireEncryption" in data:
        out["require_encryption"] = data["RequireEncryption"]
    if "CreatedTimestamp" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["created_timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "UpdatedTimestamp" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["updated_timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    if "VoiceConnectorArn" in data:
        out["voice_connector_arn"] = data["VoiceConnectorArn"]
    if "IntegrationType" in data:
        import aws_sdk_chime_sdk_voice.types.voice_connector_integration_type

        out["integration_type"] = (
            aws_sdk_chime_sdk_voice.types.voice_connector_integration_type.deserialize_json(
                data["IntegrationType"]
            )
        )
    if "NetworkType" in data:
        import aws_sdk_chime_sdk_voice.types.network_type

        out["network_type"] = (
            aws_sdk_chime_sdk_voice.types.network_type.deserialize_json(
                data["NetworkType"]
            )
        )
    return out
