"""Generated from Smithy shape ``com.amazonaws.mediatailor#SourceLocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__list_of_segment_delivery_configuration
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.__timestamp_unix
    import aws_sdk_mediatailor.types.access_configuration
    import aws_sdk_mediatailor.types.default_segment_delivery_configuration
    import aws_sdk_mediatailor.types.http_configuration


class SourceLocation(TypedDict):
    access_configuration: NotRequired[
        "aws_sdk_mediatailor.types.access_configuration.AccessConfiguration"
    ]
    """<p>The access configuration for the source location.</p>"""
    arn: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The ARN of the SourceLocation.</p>"""
    creation_time: NotRequired[
        "aws_sdk_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp that indicates when the source location was created.</p>"""
    default_segment_delivery_configuration: NotRequired[
        "aws_sdk_mediatailor.types.default_segment_delivery_configuration.DefaultSegmentDeliveryConfiguration"
    ]
    """<p>The default segment delivery configuration.</p>"""
    http_configuration: "aws_sdk_mediatailor.types.http_configuration.HttpConfiguration"
    """<p>The HTTP configuration for the source location.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp that indicates when the source location was last modified.</p>"""
    segment_delivery_configurations: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_segment_delivery_configuration.__listOfSegmentDeliveryConfiguration"
    ]
    """<p>The segment delivery configurations for the source location.</p>"""
    source_location_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the source location.</p>"""
    tags: NotRequired["aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags assigned to the source location. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceLocation) -> dict:
    out: dict = {}
    if "access_configuration" in value:
        import aws_sdk_mediatailor.types.access_configuration

        out["AccessConfiguration"] = (
            aws_sdk_mediatailor.types.access_configuration.serialize_json(
                value["access_configuration"]
            )
        )
    out["Arn"] = value["arn"]
    if "creation_time" in value:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["CreationTime"] = aws_sdk_mediatailor.types.__timestamp_unix.serialize_json(
            value["creation_time"]
        )
    if "default_segment_delivery_configuration" in value:
        import aws_sdk_mediatailor.types.default_segment_delivery_configuration

        out["DefaultSegmentDeliveryConfiguration"] = (
            aws_sdk_mediatailor.types.default_segment_delivery_configuration.serialize_json(
                value["default_segment_delivery_configuration"]
            )
        )
    import aws_sdk_mediatailor.types.http_configuration

    out["HttpConfiguration"] = (
        aws_sdk_mediatailor.types.http_configuration.serialize_json(
            value["http_configuration"]
        )
    )
    if "last_modified_time" in value:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["LastModifiedTime"] = (
            aws_sdk_mediatailor.types.__timestamp_unix.serialize_json(
                value["last_modified_time"]
            )
        )
    if "segment_delivery_configurations" in value:
        import aws_sdk_mediatailor.types.__list_of_segment_delivery_configuration

        out["SegmentDeliveryConfigurations"] = (
            aws_sdk_mediatailor.types.__list_of_segment_delivery_configuration.serialize_json(
                value["segment_delivery_configurations"]
            )
        )
    out["SourceLocationName"] = value["source_location_name"]
    if "tags" in value:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> SourceLocation:
    out: SourceLocation = {}  # type: ignore[typeddict-item]
    if "AccessConfiguration" in data:
        import aws_sdk_mediatailor.types.access_configuration

        out["access_configuration"] = (
            aws_sdk_mediatailor.types.access_configuration.deserialize_json(
                data["AccessConfiguration"]
            )
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("SourceLocation.arn required")
    if "CreationTime" in data:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["creation_time"] = (
            aws_sdk_mediatailor.types.__timestamp_unix.deserialize_json(
                data["CreationTime"]
            )
        )
    if "DefaultSegmentDeliveryConfiguration" in data:
        import aws_sdk_mediatailor.types.default_segment_delivery_configuration

        out["default_segment_delivery_configuration"] = (
            aws_sdk_mediatailor.types.default_segment_delivery_configuration.deserialize_json(
                data["DefaultSegmentDeliveryConfiguration"]
            )
        )
    if "HttpConfiguration" in data:
        import aws_sdk_mediatailor.types.http_configuration

        out["http_configuration"] = (
            aws_sdk_mediatailor.types.http_configuration.deserialize_json(
                data["HttpConfiguration"]
            )
        )
    else:
        raise DeserializationError("SourceLocation.http_configuration required")
    if "LastModifiedTime" in data:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["last_modified_time"] = (
            aws_sdk_mediatailor.types.__timestamp_unix.deserialize_json(
                data["LastModifiedTime"]
            )
        )
    if "SegmentDeliveryConfigurations" in data:
        import aws_sdk_mediatailor.types.__list_of_segment_delivery_configuration

        out["segment_delivery_configurations"] = (
            aws_sdk_mediatailor.types.__list_of_segment_delivery_configuration.deserialize_json(
                data["SegmentDeliveryConfigurations"]
            )
        )
    if "SourceLocationName" in data:
        out["source_location_name"] = data["SourceLocationName"]
    else:
        raise DeserializationError("SourceLocation.source_location_name required")
    if "tags" in data:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
