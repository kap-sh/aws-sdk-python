"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeInstanceProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.instance_profile_list
    import capo_database_migration_service.types.string


class DescribeInstanceProfilesResponse(TypedDict, closed=True):
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>Marker</code> is returned by a previous response, there are more results available. The value of <code>Marker</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>"""
    instance_profiles: NotRequired[
        "capo_database_migration_service.types.instance_profile_list.InstanceProfileList"
    ]
    """<p>A description of instance profiles.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInstanceProfilesResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "instance_profiles" in value:
        import capo_database_migration_service.types.instance_profile_list

        out["InstanceProfiles"] = (
            capo_database_migration_service.types.instance_profile_list.serialize_aws_json_1_1(
                value["instance_profiles"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInstanceProfilesResponse:
    out: DescribeInstanceProfilesResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "InstanceProfiles" in data:
        import capo_database_migration_service.types.instance_profile_list

        out["instance_profiles"] = (
            capo_database_migration_service.types.instance_profile_list.deserialize_aws_json_1_1(
                data["InstanceProfiles"]
            )
        )
    return out
