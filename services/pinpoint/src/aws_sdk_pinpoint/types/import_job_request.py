"""Generated from Smithy shape ``com.amazonaws.pinpoint#ImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__boolean
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.format


class ImportJobRequest(TypedDict, closed=True):
    define_segment: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether to create a segment that contains the endpoints, when the endpoint definitions are imported.</p>"""
    external_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>(Deprecated) Your AWS account ID, which you assigned to an external ID key in an IAM trust policy. Amazon Pinpoint previously used this value to assume an IAM role when importing endpoint definitions, but we removed this requirement. We don't recommend use of external IDs for IAM roles that are assumed by Amazon Pinpoint.</p>"""
    format: NotRequired["aws_sdk_pinpoint.types.format.Format"]
    """<p>The format of the files that contain the endpoint definitions to import. Valid values are: CSV, for comma-separated values format; and, JSON, for newline-delimited JSON format. If the Amazon S3 location stores multiple files that use different formats, Amazon Pinpoint imports data only from the files that use the specified format.</p>"""
    register_endpoints: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether to register the endpoints with Amazon Pinpoint, when the endpoint definitions are imported.</p>"""
    role_arn: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorizes Amazon Pinpoint to access the Amazon S3 location to import endpoint definitions from.</p>"""
    s3_url: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The URL of the Amazon Simple Storage Service (Amazon S3) bucket that contains the endpoint definitions to import. This location can be a folder or a single file. If the location is a folder, Amazon Pinpoint imports endpoint definitions from the files in this location, including any subfolders that the folder contains.</p> <p>The URL should be in the following format: s3://<replaceable>bucket-name</replaceable>/<replaceable>folder-name</replaceable>/<replaceable>file-name</replaceable>. The location can end with the key for an individual object or a prefix that qualifies multiple objects.</p>"""
    segment_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The identifier for the segment to update or add the imported endpoint definitions to, if the import job is meant to update an existing segment.</p>"""
    segment_name: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>A custom name for the segment that's created by the import job, if the value of the DefineSegment property is true.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportJobRequest) -> dict:
    out: dict = {}
    if "define_segment" in value:
        out["DefineSegment"] = value["define_segment"]
    if "external_id" in value:
        out["ExternalId"] = value["external_id"]
    if "format" in value:
        import aws_sdk_pinpoint.types.format

        out["Format"] = aws_sdk_pinpoint.types.format.serialize_json(value["format"])
    if "register_endpoints" in value:
        out["RegisterEndpoints"] = value["register_endpoints"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "s3_url" in value:
        out["S3Url"] = value["s3_url"]
    if "segment_id" in value:
        out["SegmentId"] = value["segment_id"]
    if "segment_name" in value:
        out["SegmentName"] = value["segment_name"]
    return out


def deserialize_json(data: dict) -> ImportJobRequest:
    out: ImportJobRequest = {}  # type: ignore[typeddict-item]
    if "DefineSegment" in data:
        out["define_segment"] = data["DefineSegment"]
    if "ExternalId" in data:
        out["external_id"] = data["ExternalId"]
    if "Format" in data:
        import aws_sdk_pinpoint.types.format

        out["format"] = aws_sdk_pinpoint.types.format.deserialize_json(data["Format"])
    if "RegisterEndpoints" in data:
        out["register_endpoints"] = data["RegisterEndpoints"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "S3Url" in data:
        out["s3_url"] = data["S3Url"]
    if "SegmentId" in data:
        out["segment_id"] = data["SegmentId"]
    if "SegmentName" in data:
        out["segment_name"] = data["SegmentName"]
    return out
