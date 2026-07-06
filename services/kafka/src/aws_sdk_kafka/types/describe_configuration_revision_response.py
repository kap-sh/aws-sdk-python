"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeConfigurationRevisionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__blob
    import aws_sdk_kafka.types.__long
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.__timestamp_iso8601


class DescribeConfigurationRevisionResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the configuration.</p>"""
    creation_time: NotRequired[
        "aws_sdk_kafka.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time when the configuration was created.</p>"""
    description: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The description of the configuration.</p>"""
    revision: NotRequired["aws_sdk_kafka.types.__long.__long"]
    """<p>The revision number.</p>"""
    server_properties: NotRequired["aws_sdk_kafka.types.__blob.__blob"]
    """<p>Contents of the <filename>server.properties</filename> file. When using the API, you must ensure that the contents of the file are base64 encoded. When using the AWS Management Console, the SDK, or the AWS CLI, the contents of <filename>server.properties</filename> can be in plaintext.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConfigurationRevisionResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "creation_time" in value:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["creationTime"] = aws_sdk_kafka.types.__timestamp_iso8601.serialize_json(
            value["creation_time"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "server_properties" in value:
        import aws_sdk_kafka.types.__blob

        out["serverProperties"] = aws_sdk_kafka.types.__blob.serialize_json(
            value["server_properties"]
        )
    return out


def deserialize_json(data: dict) -> DescribeConfigurationRevisionResponse:
    out: DescribeConfigurationRevisionResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "creationTime" in data:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["creation_time"] = aws_sdk_kafka.types.__timestamp_iso8601.deserialize_json(
            data["creationTime"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "revision" in data:
        out["revision"] = data["revision"]
    if "serverProperties" in data:
        import aws_sdk_kafka.types.__blob

        out["server_properties"] = aws_sdk_kafka.types.__blob.deserialize_json(
            data["serverProperties"]
        )
    return out
