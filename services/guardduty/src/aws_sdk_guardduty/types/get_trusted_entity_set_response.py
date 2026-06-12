"""Generated from Smithy shape ``com.amazonaws.guardduty#GetTrustedEntitySetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.expected_bucket_owner
    import aws_sdk_guardduty.types.location
    import aws_sdk_guardduty.types.name
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.tag_map
    import aws_sdk_guardduty.types.timestamp
    import aws_sdk_guardduty.types.trusted_entity_set_format
    import aws_sdk_guardduty.types.trusted_entity_set_status


class GetTrustedEntitySetResponse(TypedDict):
    name: NotRequired["aws_sdk_guardduty.types.name.Name"]
    """<p>The name of the threat entity set associated with the specified <code>trustedEntitySetId</code>.</p>"""
    format: NotRequired[
        "aws_sdk_guardduty.types.trusted_entity_set_format.TrustedEntitySetFormat"
    ]
    """<p>The format of the file that contains the trusted entity set.</p>"""
    location: NotRequired["aws_sdk_guardduty.types.location.Location"]
    """<p>The URI of the file that contains the trusted entity set.</p>"""
    expected_bucket_owner: NotRequired[
        "aws_sdk_guardduty.types.expected_bucket_owner.ExpectedBucketOwner"
    ]
    """<p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>"""
    status: NotRequired[
        "aws_sdk_guardduty.types.trusted_entity_set_status.TrustedEntitySetStatus"
    ]
    """<p>The status of the associated trusted entity set.</p>"""
    tags: NotRequired["aws_sdk_guardduty.types.tag_map.TagMap"]
    """<p>The tags associated with trusted entity set resource.</p>"""
    created_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the associated trusted entity set was created.</p>"""
    updated_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the associated trusted entity set was updated.</p>"""
    error_details: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The error details when the status is shown as <code>ERROR</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTrustedEntitySetResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "format" in value:
        import aws_sdk_guardduty.types.trusted_entity_set_format

        out["format"] = (
            aws_sdk_guardduty.types.trusted_entity_set_format.serialize_json(
                value["format"]
            )
        )
    if "location" in value:
        out["location"] = value["location"]
    if "expected_bucket_owner" in value:
        out["expectedBucketOwner"] = value["expected_bucket_owner"]
    if "status" in value:
        import aws_sdk_guardduty.types.trusted_entity_set_status

        out["status"] = (
            aws_sdk_guardduty.types.trusted_entity_set_status.serialize_json(
                value["status"]
            )
        )
    if "tags" in value:
        import aws_sdk_guardduty.types.tag_map

        out["tags"] = aws_sdk_guardduty.types.tag_map.serialize_json(value["tags"])
    if "created_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["createdAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["updatedAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "error_details" in value:
        out["errorDetails"] = value["error_details"]
    return out


def deserialize_json(data: dict) -> GetTrustedEntitySetResponse:
    out: GetTrustedEntitySetResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "format" in data:
        import aws_sdk_guardduty.types.trusted_entity_set_format

        out["format"] = (
            aws_sdk_guardduty.types.trusted_entity_set_format.deserialize_json(
                data["format"]
            )
        )
    if "location" in data:
        out["location"] = data["location"]
    if "expectedBucketOwner" in data:
        out["expected_bucket_owner"] = data["expectedBucketOwner"]
    if "status" in data:
        import aws_sdk_guardduty.types.trusted_entity_set_status

        out["status"] = (
            aws_sdk_guardduty.types.trusted_entity_set_status.deserialize_json(
                data["status"]
            )
        )
    if "tags" in data:
        import aws_sdk_guardduty.types.tag_map

        out["tags"] = aws_sdk_guardduty.types.tag_map.deserialize_json(data["tags"])
    if "createdAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["created_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["updated_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "errorDetails" in data:
        out["error_details"] = data["errorDetails"]
    return out
