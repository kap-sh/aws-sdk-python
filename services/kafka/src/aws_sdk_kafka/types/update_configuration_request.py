"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__blob
    import aws_sdk_kafka.types.__string


class UpdateConfigurationRequest(TypedDict, closed=True):
    arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the configuration.</p>"""
    description: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The description of the configuration revision.</p>"""
    server_properties: NotRequired["aws_sdk_kafka.types.__blob.__blob"]
    """<p>Contents of the <filename>server.properties</filename> file. When using the API, you must ensure that the contents of the file are base64 encoded. When using the AWS Management Console, the SDK, or the AWS CLI, the contents of <filename>server.properties</filename> can be in plaintext.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "server_properties" in value:
        import aws_sdk_kafka.types.__blob

        out["serverProperties"] = aws_sdk_kafka.types.__blob.serialize_json(
            value["server_properties"]
        )
    return out


def deserialize_json(data: dict) -> UpdateConfigurationRequest:
    out: UpdateConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "serverProperties" in data:
        import aws_sdk_kafka.types.__blob

        out["server_properties"] = aws_sdk_kafka.types.__blob.deserialize_json(
            data["serverProperties"]
        )
    return out
