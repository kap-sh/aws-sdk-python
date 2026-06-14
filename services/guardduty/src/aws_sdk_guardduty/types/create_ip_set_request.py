"""Generated from Smithy shape ``com.amazonaws.guardduty#CreateIPSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.account_id
    import aws_sdk_guardduty.types.boolean
    import aws_sdk_guardduty.types.client_token
    import aws_sdk_guardduty.types.detector_id
    import aws_sdk_guardduty.types.ip_set_format
    import aws_sdk_guardduty.types.location
    import aws_sdk_guardduty.types.name
    import aws_sdk_guardduty.types.tag_map


class CreateIPSetRequest(TypedDict):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    r"""<p>The unique ID of the detector of the GuardDuty account for which you want to create an IPSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""
    name: NotRequired["aws_sdk_guardduty.types.name.Name"]
    """<p>The user-friendly name to identify the IPSet.</p> <p> Allowed characters are alphanumeric, whitespace, dash (-), and underscores (_).</p>"""
    format: NotRequired["aws_sdk_guardduty.types.ip_set_format.IpSetFormat"]
    """<p>The format of the file that contains the IPSet.</p>"""
    location: NotRequired["aws_sdk_guardduty.types.location.Location"]
    """<p>The URI of the file that contains the IPSet. </p>"""
    activate: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
    """<p>A Boolean value that indicates whether GuardDuty is to start using the uploaded IPSet.</p>"""
    client_token: NotRequired["aws_sdk_guardduty.types.client_token.ClientToken"]
    """<p>The idempotency token for the create request.</p>"""
    tags: NotRequired["aws_sdk_guardduty.types.tag_map.TagMap"]
    """<p>The tags to be added to a new IP set resource.</p>"""
    expected_bucket_owner: NotRequired["aws_sdk_guardduty.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIPSetRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "format" in value:
        import aws_sdk_guardduty.types.ip_set_format

        out["format"] = aws_sdk_guardduty.types.ip_set_format.serialize_json(
            value["format"]
        )
    if "location" in value:
        out["location"] = value["location"]
    if "activate" in value:
        out["activate"] = value["activate"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_guardduty.types.tag_map

        out["tags"] = aws_sdk_guardduty.types.tag_map.serialize_json(value["tags"])
    if "expected_bucket_owner" in value:
        out["expectedBucketOwner"] = value["expected_bucket_owner"]
    return out


def deserialize_json(data: dict) -> CreateIPSetRequest:
    out: CreateIPSetRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "format" in data:
        import aws_sdk_guardduty.types.ip_set_format

        out["format"] = aws_sdk_guardduty.types.ip_set_format.deserialize_json(
            data["format"]
        )
    if "location" in data:
        out["location"] = data["location"]
    if "activate" in data:
        out["activate"] = data["activate"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_guardduty.types.tag_map

        out["tags"] = aws_sdk_guardduty.types.tag_map.deserialize_json(data["tags"])
    if "expectedBucketOwner" in data:
        out["expected_bucket_owner"] = data["expectedBucketOwner"]
    return out
