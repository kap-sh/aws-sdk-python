"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeApplicableIndividualAssessmentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.individual_assessment_name_list
    import aws_sdk_database_migration_service.types.string


class DescribeApplicableIndividualAssessmentsResponse(TypedDict):
    individual_assessment_names: NotRequired[
        "aws_sdk_database_migration_service.types.individual_assessment_name_list.IndividualAssessmentNameList"
    ]
    """<p>List of names for the individual assessments supported by the premigration assessment run that you start based on the specified request parameters. For more information on the available individual assessments, including compatibility with different migration task configurations, see <a href=\"https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.html\">Working with premigration assessment runs</a> in the <i>Database Migration Service User Guide.</i> </p>"""
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>Pagination token returned for you to pass to a subsequent request. If you pass this token as the <code>Marker</code> value in a subsequent request, the response includes only records beyond the marker, up to the value specified in the request by <code>MaxRecords</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeApplicableIndividualAssessmentsResponse,
) -> dict:
    out: dict = {}
    if "individual_assessment_names" in value:
        import aws_sdk_database_migration_service.types.individual_assessment_name_list

        out["IndividualAssessmentNames"] = (
            aws_sdk_database_migration_service.types.individual_assessment_name_list.serialize_aws_json_1_1(
                value["individual_assessment_names"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeApplicableIndividualAssessmentsResponse:
    out: DescribeApplicableIndividualAssessmentsResponse = {}  # type: ignore[typeddict-item]
    if "IndividualAssessmentNames" in data:
        import aws_sdk_database_migration_service.types.individual_assessment_name_list

        out["individual_assessment_names"] = (
            aws_sdk_database_migration_service.types.individual_assessment_name_list.deserialize_aws_json_1_1(
                data["IndividualAssessmentNames"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
