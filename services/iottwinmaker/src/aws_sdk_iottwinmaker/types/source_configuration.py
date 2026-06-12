"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SourceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration
    import aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration
    import aws_sdk_iottwinmaker.types.s3_source_configuration
    import aws_sdk_iottwinmaker.types.source_type


class SourceConfiguration(TypedDict):
    type: "aws_sdk_iottwinmaker.types.source_type.SourceType"
    """<p>The source configuration type.</p>"""
    s3_configuration: NotRequired[
        "aws_sdk_iottwinmaker.types.s3_source_configuration.S3SourceConfiguration"
    ]
    """<p>The source configuration S3 configuration.</p>"""
    iot_site_wise_configuration: NotRequired[
        "aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration.IotSiteWiseSourceConfiguration"
    ]
    """<p>The source configuration IoT SiteWise configuration.</p>"""
    iot_twin_maker_configuration: NotRequired[
        "aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration.IotTwinMakerSourceConfiguration"
    ]
    """<p>The source configuration IoT TwinMaker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceConfiguration) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "s3_configuration" in value:
        import aws_sdk_iottwinmaker.types.s3_source_configuration

        out["s3Configuration"] = (
            aws_sdk_iottwinmaker.types.s3_source_configuration.serialize_json(
                value["s3_configuration"]
            )
        )
    if "iot_site_wise_configuration" in value:
        import aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration

        out["iotSiteWiseConfiguration"] = (
            aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration.serialize_json(
                value["iot_site_wise_configuration"]
            )
        )
    if "iot_twin_maker_configuration" in value:
        import aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration

        out["iotTwinMakerConfiguration"] = (
            aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration.serialize_json(
                value["iot_twin_maker_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SourceConfiguration:
    out: SourceConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("SourceConfiguration.type required")
    if "s3Configuration" in data:
        import aws_sdk_iottwinmaker.types.s3_source_configuration

        out["s3_configuration"] = (
            aws_sdk_iottwinmaker.types.s3_source_configuration.deserialize_json(
                data["s3Configuration"]
            )
        )
    if "iotSiteWiseConfiguration" in data:
        import aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration

        out["iot_site_wise_configuration"] = (
            aws_sdk_iottwinmaker.types.iot_site_wise_source_configuration.deserialize_json(
                data["iotSiteWiseConfiguration"]
            )
        )
    if "iotTwinMakerConfiguration" in data:
        import aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration

        out["iot_twin_maker_configuration"] = (
            aws_sdk_iottwinmaker.types.iot_twin_maker_source_configuration.deserialize_json(
                data["iotTwinMakerConfiguration"]
            )
        )
    return out
