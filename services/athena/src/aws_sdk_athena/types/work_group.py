"""Generated from Smithy shape ``com.amazonaws.athena#WorkGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.date
    import aws_sdk_athena.types.identity_center_application_arn
    import aws_sdk_athena.types.work_group_configuration
    import aws_sdk_athena.types.work_group_description_string
    import aws_sdk_athena.types.work_group_name
    import aws_sdk_athena.types.work_group_state


class WorkGroup(TypedDict, closed=True):
    name: "aws_sdk_athena.types.work_group_name.WorkGroupName"
    """<p>The workgroup name.</p>"""
    state: NotRequired["aws_sdk_athena.types.work_group_state.WorkGroupState"]
    """<p>The state of the workgroup: ENABLED or DISABLED.</p>"""
    configuration: NotRequired[
        "aws_sdk_athena.types.work_group_configuration.WorkGroupConfiguration"
    ]
    """<p>The configuration of the workgroup, which includes the location in Amazon S3 where query and calculation results are stored, the encryption configuration, if any, used for query and calculation results; whether the Amazon CloudWatch Metrics are enabled for the workgroup; whether workgroup settings override client-side settings; and the data usage limits for the amount of data scanned per query or per workgroup. The workgroup settings override is specified in <code>EnforceWorkGroupConfiguration</code> (true/false) in the <code>WorkGroupConfiguration</code>. See <a>WorkGroupConfiguration$EnforceWorkGroupConfiguration</a>.</p>"""
    description: NotRequired[
        "aws_sdk_athena.types.work_group_description_string.WorkGroupDescriptionString"
    ]
    """<p>The workgroup description.</p>"""
    creation_time: NotRequired["aws_sdk_athena.types.date.Date"]
    """<p>The date and time the workgroup was created.</p>"""
    identity_center_application_arn: NotRequired[
        "aws_sdk_athena.types.identity_center_application_arn.IdentityCenterApplicationArn"
    ]
    """<p>The ARN of the IAM Identity Center enabled application associated with the workgroup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkGroup) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "state" in value:
        import aws_sdk_athena.types.work_group_state

        out["State"] = aws_sdk_athena.types.work_group_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "configuration" in value:
        import aws_sdk_athena.types.work_group_configuration

        out["Configuration"] = (
            aws_sdk_athena.types.work_group_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "creation_time" in value:
        import aws_sdk_athena.types.date

        out["CreationTime"] = aws_sdk_athena.types.date.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "identity_center_application_arn" in value:
        out["IdentityCenterApplicationArn"] = value["identity_center_application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkGroup:
    out: WorkGroup = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("WorkGroup.name required")
    if "State" in data:
        import aws_sdk_athena.types.work_group_state

        out["state"] = aws_sdk_athena.types.work_group_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "Configuration" in data:
        import aws_sdk_athena.types.work_group_configuration

        out["configuration"] = (
            aws_sdk_athena.types.work_group_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreationTime" in data:
        import aws_sdk_athena.types.date

        out["creation_time"] = aws_sdk_athena.types.date.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "IdentityCenterApplicationArn" in data:
        out["identity_center_application_arn"] = data["IdentityCenterApplicationArn"]
    return out
