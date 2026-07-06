"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.destination_type
    import aws_sdk_iottwinmaker.types.iot_twin_maker_destination_configuration
    import aws_sdk_iottwinmaker.types.s3_destination_configuration


class DestinationConfiguration(TypedDict, closed=True):
    type: "aws_sdk_iottwinmaker.types.destination_type.DestinationType"
    """<p>The destination type.</p>"""
    s3_configuration: NotRequired[
        "aws_sdk_iottwinmaker.types.s3_destination_configuration.S3DestinationConfiguration"
    ]
    """<p>The metadata transfer job S3 configuration. [need to add S3 entity]</p>"""
    iot_twin_maker_configuration: NotRequired[
        "aws_sdk_iottwinmaker.types.iot_twin_maker_destination_configuration.IotTwinMakerDestinationConfiguration"
    ]
    """<p>The metadata transfer job Amazon Web Services IoT TwinMaker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationConfiguration) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "s3_configuration" in value:
        import aws_sdk_iottwinmaker.types.s3_destination_configuration

        out["s3Configuration"] = (
            aws_sdk_iottwinmaker.types.s3_destination_configuration.serialize_json(
                value["s3_configuration"]
            )
        )
    if "iot_twin_maker_configuration" in value:
        import aws_sdk_iottwinmaker.types.iot_twin_maker_destination_configuration

        out["iotTwinMakerConfiguration"] = (
            aws_sdk_iottwinmaker.types.iot_twin_maker_destination_configuration.serialize_json(
                value["iot_twin_maker_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DestinationConfiguration:
    out: DestinationConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("DestinationConfiguration.type required")
    if "s3Configuration" in data:
        import aws_sdk_iottwinmaker.types.s3_destination_configuration

        out["s3_configuration"] = (
            aws_sdk_iottwinmaker.types.s3_destination_configuration.deserialize_json(
                data["s3Configuration"]
            )
        )
    if "iotTwinMakerConfiguration" in data:
        import aws_sdk_iottwinmaker.types.iot_twin_maker_destination_configuration

        out["iot_twin_maker_configuration"] = (
            aws_sdk_iottwinmaker.types.iot_twin_maker_destination_configuration.deserialize_json(
                data["iotTwinMakerConfiguration"]
            )
        )
    return out
