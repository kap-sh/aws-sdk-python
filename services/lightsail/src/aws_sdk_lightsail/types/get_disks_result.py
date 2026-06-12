"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDisksResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.disk_list
    import aws_sdk_lightsail.types.string


class GetDisksResult(TypedDict):
    disks: NotRequired["aws_sdk_lightsail.types.disk_list.DiskList"]
    """<p>An array of objects containing information about all block storage disks.</p>"""
    next_page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetDisks</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDisksResult) -> dict:
    out: dict = {}
    if "disks" in value:
        import aws_sdk_lightsail.types.disk_list

        out["disks"] = aws_sdk_lightsail.types.disk_list.serialize_aws_json_1_1(
            value["disks"]
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDisksResult:
    out: GetDisksResult = {}  # type: ignore[typeddict-item]
    if "disks" in data:
        import aws_sdk_lightsail.types.disk_list

        out["disks"] = aws_sdk_lightsail.types.disk_list.deserialize_aws_json_1_1(
            data["disks"]
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
