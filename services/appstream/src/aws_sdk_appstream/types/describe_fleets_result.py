"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeFleetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.fleet_list
    import aws_sdk_appstream.types.string


class DescribeFleetsResult(TypedDict, closed=True):
    fleets: NotRequired["aws_sdk_appstream.types.fleet_list.FleetList"]
    """<p>Information about the fleets.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetsResult) -> dict:
    out: dict = {}
    if "fleets" in value:
        import aws_sdk_appstream.types.fleet_list

        out["Fleets"] = aws_sdk_appstream.types.fleet_list.serialize_aws_json_1_1(
            value["fleets"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetsResult:
    out: DescribeFleetsResult = {}  # type: ignore[typeddict-item]
    if "Fleets" in data:
        import aws_sdk_appstream.types.fleet_list

        out["fleets"] = aws_sdk_appstream.types.fleet_list.deserialize_aws_json_1_1(
            data["Fleets"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
