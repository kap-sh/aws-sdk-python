"""Generated from Smithy shape ``com.amazonaws.pinpoint#SegmentImportResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.format
    import capo_pinpoint.types.map_of__integer


class SegmentImportResource(TypedDict, closed=True):
    channel_counts: NotRequired["capo_pinpoint.types.map_of__integer.MapOf__integer"]
    """<p>The number of channel types in the endpoint definitions that were imported to create the segment.</p>"""
    external_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>(Deprecated) Your AWS account ID, which you assigned to an external ID key in an IAM trust policy. Amazon Pinpoint previously used this value to assume an IAM role when importing endpoint definitions, but we removed this requirement. We don't recommend use of external IDs for IAM roles that are assumed by Amazon Pinpoint.</p>"""
    format: NotRequired["capo_pinpoint.types.format.Format"]
    """<p>The format of the files that were imported to create the segment. Valid values are: CSV, for comma-separated values format; and, JSON, for newline-delimited JSON format.</p>"""
    role_arn: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorized Amazon Pinpoint to access the Amazon S3 location to import endpoint definitions from.</p>"""
    s3_url: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The URL of the Amazon Simple Storage Service (Amazon S3) bucket that the endpoint definitions were imported from to create the segment.</p>"""
    size: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The number of endpoint definitions that were imported successfully to create the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentImportResource) -> dict:
    out: dict = {}
    if "channel_counts" in value:
        import capo_pinpoint.types.map_of__integer

        out["ChannelCounts"] = capo_pinpoint.types.map_of__integer.serialize_json(
            value["channel_counts"]
        )
    if "external_id" in value:
        out["ExternalId"] = value["external_id"]
    if "format" in value:
        import capo_pinpoint.types.format

        out["Format"] = capo_pinpoint.types.format.serialize_json(value["format"])
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "s3_url" in value:
        out["S3Url"] = value["s3_url"]
    if "size" in value:
        out["Size"] = value["size"]
    return out


def deserialize_json(data: dict) -> SegmentImportResource:
    out: SegmentImportResource = {}  # type: ignore[typeddict-item]
    if "ChannelCounts" in data:
        import capo_pinpoint.types.map_of__integer

        out["channel_counts"] = capo_pinpoint.types.map_of__integer.deserialize_json(
            data["ChannelCounts"]
        )
    if "ExternalId" in data:
        out["external_id"] = data["ExternalId"]
    if "Format" in data:
        import capo_pinpoint.types.format

        out["format"] = capo_pinpoint.types.format.deserialize_json(data["Format"])
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "S3Url" in data:
        out["s3_url"] = data["S3Url"]
    if "Size" in data:
        out["size"] = data["Size"]
    return out
