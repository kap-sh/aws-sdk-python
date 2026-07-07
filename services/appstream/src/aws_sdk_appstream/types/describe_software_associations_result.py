"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeSoftwareAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.arn
    import aws_sdk_appstream.types.software_associations_list
    import aws_sdk_appstream.types.string


class DescribeSoftwareAssociationsResult(TypedDict, closed=True):
    associated_resource: NotRequired["aws_sdk_appstream.types.arn.Arn"]
    """<p>The ARN of the resource to describe software associations.</p>"""
    software_associations: NotRequired[
        "aws_sdk_appstream.types.software_associations_list.SoftwareAssociationsList"
    ]
    """<p>Collection of license included applications association details including:</p> <ul> <li> <p>License included application name and version information</p> </li> <li> <p>Deployment status (SoftwareDeploymentStatus enum)</p> </li> <li> <p>Error details for failed deployments</p> </li> <li> <p>Association timestamps</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSoftwareAssociationsResult) -> dict:
    out: dict = {}
    if "associated_resource" in value:
        out["AssociatedResource"] = value["associated_resource"]
    if "software_associations" in value:
        import aws_sdk_appstream.types.software_associations_list

        out["SoftwareAssociations"] = (
            aws_sdk_appstream.types.software_associations_list.serialize_aws_json_1_1(
                value["software_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSoftwareAssociationsResult:
    out: DescribeSoftwareAssociationsResult = {}  # type: ignore[typeddict-item]
    if "AssociatedResource" in data:
        out["associated_resource"] = data["AssociatedResource"]
    if "SoftwareAssociations" in data:
        import aws_sdk_appstream.types.software_associations_list

        out["software_associations"] = (
            aws_sdk_appstream.types.software_associations_list.deserialize_aws_json_1_1(
                data["SoftwareAssociations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
