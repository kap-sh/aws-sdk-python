"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetApplicationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.applications_info_list


class BatchGetApplicationsOutput(TypedDict, closed=True):
    applications_info: NotRequired[
        "capo_codedeploy.types.applications_info_list.ApplicationsInfoList"
    ]
    """<p>Information about the applications.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetApplicationsOutput) -> dict:
    out: dict = {}
    if "applications_info" in value:
        import capo_codedeploy.types.applications_info_list

        out["applicationsInfo"] = (
            capo_codedeploy.types.applications_info_list.serialize_aws_json_1_1(
                value["applications_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetApplicationsOutput:
    out: BatchGetApplicationsOutput = {}  # type: ignore[typeddict-item]
    if "applicationsInfo" in data:
        import capo_codedeploy.types.applications_info_list

        out["applications_info"] = (
            capo_codedeploy.types.applications_info_list.deserialize_aws_json_1_1(
                data["applicationsInfo"]
            )
        )
    return out
