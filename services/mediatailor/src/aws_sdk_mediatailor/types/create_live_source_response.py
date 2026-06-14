"""Generated from Smithy shape ``com.amazonaws.mediatailor#CreateLiveSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.__timestamp_unix
    import aws_sdk_mediatailor.types.http_package_configurations


class CreateLiveSourceResponse(TypedDict):
    arn: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The ARN to assign to the live source.</p>"""
    creation_time: NotRequired[
        "aws_sdk_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The time the live source was created.</p>"""
    http_package_configurations: NotRequired[
        "aws_sdk_mediatailor.types.http_package_configurations.HttpPackageConfigurations"
    ]
    """<p>A list of HTTP package configuration parameters for this live source.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The time the live source was last modified.</p>"""
    live_source_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name to assign to the live source.</p>"""
    source_location_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name to assign to the source location of the live source.</p>"""
    tags: NotRequired["aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"]
    r"""<p>The tags to assign to the live source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLiveSourceResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_time" in value:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["CreationTime"] = aws_sdk_mediatailor.types.__timestamp_unix.serialize_json(
            value["creation_time"]
        )
    if "http_package_configurations" in value:
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
    if "live_source_name" in value:
        out["LiveSourceName"] = value["live_source_name"]
    if "source_location_name" in value:
        out["SourceLocationName"] = value["source_location_name"]
    if "tags" in value:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateLiveSourceResponse:
    out: CreateLiveSourceResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
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
    if "LastModifiedTime" in data:
        import aws_sdk_mediatailor.types.__timestamp_unix

        out["last_modified_time"] = (
            aws_sdk_mediatailor.types.__timestamp_unix.deserialize_json(
                data["LastModifiedTime"]
            )
        )
    if "LiveSourceName" in data:
        out["live_source_name"] = data["LiveSourceName"]
    if "SourceLocationName" in data:
        out["source_location_name"] = data["SourceLocationName"]
    if "tags" in data:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
