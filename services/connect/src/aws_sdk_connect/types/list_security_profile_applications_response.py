"""Generated from Smithy shape ``com.amazonaws.connect#ListSecurityProfileApplicationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.applications
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.timestamp


class ListSecurityProfileApplicationsResponse(TypedDict):
    applications: NotRequired["aws_sdk_connect.types.applications.Applications"]
    """<p>A list of the third-party application's metadata.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityProfileApplicationsResponse) -> dict:
    out: dict = {}
    if "applications" in value:
        import aws_sdk_connect.types.applications

        out["Applications"] = aws_sdk_connect.types.applications.serialize_json(
            value["applications"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> ListSecurityProfileApplicationsResponse:
    out: ListSecurityProfileApplicationsResponse = {}  # type: ignore[typeddict-item]
    if "Applications" in data:
        import aws_sdk_connect.types.applications

        out["applications"] = aws_sdk_connect.types.applications.deserialize_json(
            data["Applications"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
