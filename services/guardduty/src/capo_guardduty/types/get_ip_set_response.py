"""Generated from Smithy shape ``com.amazonaws.guardduty#GetIPSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_id
    import capo_guardduty.types.ip_set_format
    import capo_guardduty.types.ip_set_status
    import capo_guardduty.types.location
    import capo_guardduty.types.name
    import capo_guardduty.types.tag_map


class GetIPSetResponse(TypedDict, closed=True):
    name: NotRequired["capo_guardduty.types.name.Name"]
    """<p>The user-friendly name for the IPSet.</p>"""
    format: NotRequired["capo_guardduty.types.ip_set_format.IpSetFormat"]
    """<p>The format of the file that contains the IPSet.</p>"""
    location: NotRequired["capo_guardduty.types.location.Location"]
    """<p>The URI of the file that contains the IPSet.</p>"""
    status: NotRequired["capo_guardduty.types.ip_set_status.IpSetStatus"]
    """<p>The status of IPSet file that was uploaded.</p>"""
    tags: NotRequired["capo_guardduty.types.tag_map.TagMap"]
    """<p>The tags of the IPSet resource.</p>"""
    expected_bucket_owner: NotRequired["capo_guardduty.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter. This field appears in the response only if it was provided during IPSet creation or update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIPSetResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "format" in value:
        import capo_guardduty.types.ip_set_format

        out["format"] = capo_guardduty.types.ip_set_format.serialize_json(
            value["format"]
        )
    if "location" in value:
        out["location"] = value["location"]
    if "status" in value:
        import capo_guardduty.types.ip_set_status

        out["status"] = capo_guardduty.types.ip_set_status.serialize_json(
            value["status"]
        )
    if "tags" in value:
        import capo_guardduty.types.tag_map

        out["tags"] = capo_guardduty.types.tag_map.serialize_json(value["tags"])
    if "expected_bucket_owner" in value:
        out["expectedBucketOwner"] = value["expected_bucket_owner"]
    return out


def deserialize_json(data: dict) -> GetIPSetResponse:
    out: GetIPSetResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "format" in data:
        import capo_guardduty.types.ip_set_format

        out["format"] = capo_guardduty.types.ip_set_format.deserialize_json(
            data["format"]
        )
    if "location" in data:
        out["location"] = data["location"]
    if "status" in data:
        import capo_guardduty.types.ip_set_status

        out["status"] = capo_guardduty.types.ip_set_status.deserialize_json(
            data["status"]
        )
    if "tags" in data:
        import capo_guardduty.types.tag_map

        out["tags"] = capo_guardduty.types.tag_map.deserialize_json(data["tags"])
    if "expectedBucketOwner" in data:
        out["expected_bucket_owner"] = data["expectedBucketOwner"]
    return out
