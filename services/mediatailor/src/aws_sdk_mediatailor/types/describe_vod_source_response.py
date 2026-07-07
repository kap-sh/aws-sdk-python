"""Generated from Smithy shape ``com.amazonaws.mediatailor#DescribeVodSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.__timestamp_unix
    import aws_sdk_mediatailor.types.ad_break_opportunities
    import aws_sdk_mediatailor.types.http_package_configurations


class DescribeVodSourceResponse(TypedDict, closed=True):
    ad_break_opportunities: NotRequired[
        "aws_sdk_mediatailor.types.ad_break_opportunities.AdBreakOpportunities"
    ]
    """<p>The ad break opportunities within the VOD source.</p>"""
    arn: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The ARN of the VOD source.</p>"""
    creation_time: NotRequired[
        "aws_sdk_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The timestamp that indicates when the VOD source was created.</p>"""
    http_package_configurations: NotRequired[
        "aws_sdk_mediatailor.types.http_package_configurations.HttpPackageConfigurations"
    ]
    """<p>The HTTP package configurations.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_mediatailor.types.__timestamp_unix.__timestampUnix"
    ]
    """<p>The last modified time of the VOD source.</p>"""
    source_location_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name of the source location associated with the VOD source.</p>"""
    tags: NotRequired["aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"]
    r"""<p>The tags assigned to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""
    vod_source_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name of the VOD source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVodSourceResponse) -> dict:
    out: dict = {}
    if "ad_break_opportunities" in value:
        import aws_sdk_mediatailor.types.ad_break_opportunities

        out["AdBreakOpportunities"] = (
            aws_sdk_mediatailor.types.ad_break_opportunities.serialize_json(
                value["ad_break_opportunities"]
            )
        )
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
    if "source_location_name" in value:
        out["SourceLocationName"] = value["source_location_name"]
    if "tags" in value:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    if "vod_source_name" in value:
        out["VodSourceName"] = value["vod_source_name"]
    return out


def deserialize_json(data: dict) -> DescribeVodSourceResponse:
    out: DescribeVodSourceResponse = {}  # type: ignore[typeddict-item]
    if "AdBreakOpportunities" in data:
        import aws_sdk_mediatailor.types.ad_break_opportunities

        out["ad_break_opportunities"] = (
            aws_sdk_mediatailor.types.ad_break_opportunities.deserialize_json(
                data["AdBreakOpportunities"]
            )
        )
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
    if "SourceLocationName" in data:
        out["source_location_name"] = data["SourceLocationName"]
    if "tags" in data:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    if "VodSourceName" in data:
        out["vod_source_name"] = data["VodSourceName"]
    return out
