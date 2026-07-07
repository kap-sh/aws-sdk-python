"""Generated from Smithy shape ``com.amazonaws.mediatailor#VodSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.__timestamp_unix
    import aws_sdk_mediatailor.types.http_package_configurations


class VodSource(TypedDict, closed=True):
    arn: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The ARN for the VOD source.</p>"""
    creation_time: NotRequired[
        "aws_sdk_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp that indicates when the VOD source was created.</p>"""
    http_package_configurations: "aws_sdk_mediatailor.types.http_package_configurations.HttpPackageConfigurations"
    """<p>The HTTP package configurations for the VOD source.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp that indicates when the VOD source was last modified.</p>"""
    source_location_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the source location that the VOD source is associated with.</p>"""
    tags: NotRequired["aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"]
    r"""<p>The tags assigned to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""
    vod_source_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the VOD source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VodSource) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "creation_time" in value:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["CreationTime"] = aws_sdk_mediatailor.types.__timestamp_unix.serialize_json(
            value["creation_time"]
        )
    import aws_sdk_mediatailor.types.http_package_configurations

    out["HttpPackageConfigurations"] = (
        aws_sdk_mediatailor.types.http_package_configurations.serialize_json(
            value["http_package_configurations"]
        )
    )
    if "last_modified_time" in value:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["LastModifiedTime"] = (
            aws_sdk_mediatailor.types.__timestamp_unix.serialize_json(
                value["last_modified_time"]
            )
        )
    out["SourceLocationName"] = value["source_location_name"]
    if "tags" in value:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    out["VodSourceName"] = value["vod_source_name"]
    return out


def deserialize_json(data: dict) -> VodSource:
    out: VodSource = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("VodSource.arn required")
    if "CreationTime" in data:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["creation_time"] = (
            aws_sdk_mediatailor.types.__timestamp_unix.deserialize_json(
                data["CreationTime"]
            )
        )
    if "HttpPackageConfigurations" in data:
        import aws_sdk_mediatailor.types.http_package_configurations

        out["http_package_configurations"] = (
            aws_sdk_mediatailor.types.http_package_configurations.deserialize_json(
                data["HttpPackageConfigurations"]
            )
        )
    else:
        raise DeserializationError("VodSource.http_package_configurations required")
    if "LastModifiedTime" in data:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["last_modified_time"] = (
            aws_sdk_mediatailor.types.__timestamp_unix.deserialize_json(
                data["LastModifiedTime"]
            )
        )
    if "SourceLocationName" in data:
        out["source_location_name"] = data["SourceLocationName"]
    else:
        raise DeserializationError("VodSource.source_location_name required")
    if "tags" in data:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    if "VodSourceName" in data:
        out["vod_source_name"] = data["VodSourceName"]
    else:
        raise DeserializationError("VodSource.vod_source_name required")
    return out
