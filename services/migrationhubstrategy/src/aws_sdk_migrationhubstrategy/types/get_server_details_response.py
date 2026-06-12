"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetServerDetailsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.associated_applications
    import aws_sdk_migrationhubstrategy.types.server_detail
    import aws_sdk_migrationhubstrategy.types.string


class GetServerDetailsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """<p> The token you use to retrieve the next set of results, or null if there are no more results. </p>"""
    server_detail: NotRequired[
        "aws_sdk_migrationhubstrategy.types.server_detail.ServerDetail"
    ]
    """<p> Detailed information about the server. </p>"""
    associated_applications: NotRequired[
        "aws_sdk_migrationhubstrategy.types.associated_applications.AssociatedApplications"
    ]
    """<p> The associated application group the server belongs to, as defined in AWS Application Discovery Service. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServerDetailsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "server_detail" in value:
        import aws_sdk_migrationhubstrategy.types.server_detail

        out["serverDetail"] = (
            aws_sdk_migrationhubstrategy.types.server_detail.serialize_json(
                value["server_detail"]
            )
        )
    if "associated_applications" in value:
        import aws_sdk_migrationhubstrategy.types.associated_applications

        out["associatedApplications"] = (
            aws_sdk_migrationhubstrategy.types.associated_applications.serialize_json(
                value["associated_applications"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetServerDetailsResponse:
    out: GetServerDetailsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "serverDetail" in data:
        import aws_sdk_migrationhubstrategy.types.server_detail

        out["server_detail"] = (
            aws_sdk_migrationhubstrategy.types.server_detail.deserialize_json(
                data["serverDetail"]
            )
        )
    if "associatedApplications" in data:
        import aws_sdk_migrationhubstrategy.types.associated_applications

        out["associated_applications"] = (
            aws_sdk_migrationhubstrategy.types.associated_applications.deserialize_json(
                data["associatedApplications"]
            )
        )
    return out
