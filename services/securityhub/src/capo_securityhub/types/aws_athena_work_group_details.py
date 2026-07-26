"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAthenaWorkGroupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_athena_work_group_configuration_details
    import capo_securityhub.types.non_empty_string


class AwsAthenaWorkGroupDetails(TypedDict, closed=True):
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The workgroup name. </p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The workgroup description. </p>"""
    state: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Whether the workgroup is enabled or disabled. </p>"""
    configuration: NotRequired[
        "capo_securityhub.types.aws_athena_work_group_configuration_details.AwsAthenaWorkGroupConfigurationDetails"
    ]
    """<p> The configuration of the workgroup, which includes the location in Amazon Simple Storage Service (Amazon S3) where query results are stored, the encryption option, if any, used for query results, whether Amazon CloudWatch metrics are enabled for the workgroup, and the limit for the amount of bytes scanned (cutoff) per query, if it is specified. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAthenaWorkGroupDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "state" in value:
        out["State"] = value["state"]
    if "configuration" in value:
        import capo_securityhub.types.aws_athena_work_group_configuration_details

        out["Configuration"] = (
            capo_securityhub.types.aws_athena_work_group_configuration_details.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsAthenaWorkGroupDetails:
    out: AwsAthenaWorkGroupDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "State" in data:
        out["state"] = data["State"]
    if "Configuration" in data:
        import capo_securityhub.types.aws_athena_work_group_configuration_details

        out["configuration"] = (
            capo_securityhub.types.aws_athena_work_group_configuration_details.deserialize_json(
                data["Configuration"]
            )
        )
    return out
