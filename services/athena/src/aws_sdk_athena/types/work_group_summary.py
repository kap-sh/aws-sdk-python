"""Generated from Smithy shape ``com.amazonaws.athena#WorkGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.date
    import aws_sdk_athena.types.engine_version
    import aws_sdk_athena.types.identity_center_application_arn
    import aws_sdk_athena.types.work_group_description_string
    import aws_sdk_athena.types.work_group_name
    import aws_sdk_athena.types.work_group_state


class WorkGroupSummary(TypedDict, closed=True):
    name: NotRequired["aws_sdk_athena.types.work_group_name.WorkGroupName"]
    """<p>The name of the workgroup.</p>"""
    state: NotRequired["aws_sdk_athena.types.work_group_state.WorkGroupState"]
    """<p>The state of the workgroup.</p>"""
    description: NotRequired[
        "aws_sdk_athena.types.work_group_description_string.WorkGroupDescriptionString"
    ]
    """<p>The workgroup description.</p>"""
    creation_time: NotRequired["aws_sdk_athena.types.date.Date"]
    """<p>The workgroup creation date and time.</p>"""
    engine_version: NotRequired["aws_sdk_athena.types.engine_version.EngineVersion"]
    """<p>The engine version setting for all queries on the workgroup. Queries on the <code>AmazonAthenaPreviewFunctionality</code> workgroup run on the preview engine regardless of this setting.</p>"""
    identity_center_application_arn: NotRequired[
        "aws_sdk_athena.types.identity_center_application_arn.IdentityCenterApplicationArn"
    ]
    """<p>The ARN of the IAM Identity Center enabled application associated with the workgroup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkGroupSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "state" in value:
        import aws_sdk_athena.types.work_group_state

        out["State"] = aws_sdk_athena.types.work_group_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "creation_time" in value:
        import aws_sdk_athena.types.date

        out["CreationTime"] = aws_sdk_athena.types.date.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "engine_version" in value:
        import aws_sdk_athena.types.engine_version

        out["EngineVersion"] = (
            aws_sdk_athena.types.engine_version.serialize_aws_json_1_1(
                value["engine_version"]
            )
        )
    if "identity_center_application_arn" in value:
        out["IdentityCenterApplicationArn"] = value["identity_center_application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkGroupSummary:
    out: WorkGroupSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "State" in data:
        import aws_sdk_athena.types.work_group_state

        out["state"] = aws_sdk_athena.types.work_group_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreationTime" in data:
        import aws_sdk_athena.types.date

        out["creation_time"] = aws_sdk_athena.types.date.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "EngineVersion" in data:
        import aws_sdk_athena.types.engine_version

        out["engine_version"] = (
            aws_sdk_athena.types.engine_version.deserialize_aws_json_1_1(
                data["EngineVersion"]
            )
        )
    if "IdentityCenterApplicationArn" in data:
        out["identity_center_application_arn"] = data["IdentityCenterApplicationArn"]
    return out
