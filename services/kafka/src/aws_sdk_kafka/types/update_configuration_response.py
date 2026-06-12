"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.configuration_revision


class UpdateConfigurationResponse(TypedDict):
    arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the configuration.</p>"""
    latest_revision: NotRequired[
        "aws_sdk_kafka.types.configuration_revision.ConfigurationRevision"
    ]
    """<p>Latest revision of the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "latest_revision" in value:
        import aws_sdk_kafka.types.configuration_revision

        out["latestRevision"] = (
            aws_sdk_kafka.types.configuration_revision.serialize_json(
                value["latest_revision"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConfigurationResponse:
    out: UpdateConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "latestRevision" in data:
        import aws_sdk_kafka.types.configuration_revision

        out["latest_revision"] = (
            aws_sdk_kafka.types.configuration_revision.deserialize_json(
                data["latestRevision"]
            )
        )
    return out
