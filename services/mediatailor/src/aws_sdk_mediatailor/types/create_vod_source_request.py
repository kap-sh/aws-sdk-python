"""Generated from Smithy shape ``com.amazonaws.mediatailor#CreateVodSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.http_package_configurations


class CreateVodSourceRequest(TypedDict):
    http_package_configurations: "aws_sdk_mediatailor.types.http_package_configurations.HttpPackageConfigurations"
    """<p>A list of HTTP package configuration parameters for this VOD source.</p>"""
    source_location_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the source location for this VOD source.</p>"""
    tags: NotRequired["aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"]
    r"""<p>The tags to assign to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""
    vod_source_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name associated with the VOD source.&gt;</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVodSourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_mediatailor.types.http_package_configurations

    out["HttpPackageConfigurations"] = (
        aws_sdk_mediatailor.types.http_package_configurations.serialize_json(
            value["http_package_configurations"]
        )
    )
    if "tags" in value:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateVodSourceRequest:
    out: CreateVodSourceRequest = {}  # type: ignore[typeddict-item]
    if "HttpPackageConfigurations" in data:
        import aws_sdk_mediatailor.types.http_package_configurations

        out["http_package_configurations"] = (
            aws_sdk_mediatailor.types.http_package_configurations.deserialize_json(
                data["HttpPackageConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "CreateVodSourceRequest.http_package_configurations required"
        )
    if "tags" in data:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
