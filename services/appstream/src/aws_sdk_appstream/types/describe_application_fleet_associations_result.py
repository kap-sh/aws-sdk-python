"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeApplicationFleetAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.application_fleet_association_list
    import aws_sdk_appstream.types.string


class DescribeApplicationFleetAssociationsResult(TypedDict):
    application_fleet_associations: NotRequired[
        "aws_sdk_appstream.types.application_fleet_association_list.ApplicationFleetAssociationList"
    ]
    """<p>The application fleet associations in the list.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationFleetAssociationsResult) -> dict:
    out: dict = {}
    if "application_fleet_associations" in value:
        import aws_sdk_appstream.types.application_fleet_association_list

        out["ApplicationFleetAssociations"] = (
            aws_sdk_appstream.types.application_fleet_association_list.serialize_aws_json_1_1(
                value["application_fleet_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationFleetAssociationsResult:
    out: DescribeApplicationFleetAssociationsResult = {}  # type: ignore[typeddict-item]
    if "ApplicationFleetAssociations" in data:
        import aws_sdk_appstream.types.application_fleet_association_list

        out["application_fleet_associations"] = (
            aws_sdk_appstream.types.application_fleet_association_list.deserialize_aws_json_1_1(
                data["ApplicationFleetAssociations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
