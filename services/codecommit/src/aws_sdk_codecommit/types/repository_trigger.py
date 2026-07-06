"""Generated from Smithy shape ``com.amazonaws.codecommit#RepositoryTrigger``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.arn
    import aws_sdk_codecommit.types.branch_name_list
    import aws_sdk_codecommit.types.repository_trigger_custom_data
    import aws_sdk_codecommit.types.repository_trigger_event_list
    import aws_sdk_codecommit.types.repository_trigger_name


class RepositoryTrigger(TypedDict, closed=True):
    name: "aws_sdk_codecommit.types.repository_trigger_name.RepositoryTriggerName"
    """<p>The name of the trigger.</p>"""
    destination_arn: "aws_sdk_codecommit.types.arn.Arn"
    """<p>The ARN of the resource that is the target for a trigger (for example, the ARN of a topic in Amazon SNS).</p>"""
    custom_data: NotRequired[
        "aws_sdk_codecommit.types.repository_trigger_custom_data.RepositoryTriggerCustomData"
    ]
    """<p>Any custom data associated with the trigger to be included in the information sent to the target of the trigger.</p>"""
    branches: NotRequired["aws_sdk_codecommit.types.branch_name_list.BranchNameList"]
    """<p>The branches to be included in the trigger configuration. If you specify an empty array, the trigger applies to all branches.</p> <note> <p>Although no content is required in the array, you must include the array itself.</p> </note>"""
    events: "aws_sdk_codecommit.types.repository_trigger_event_list.RepositoryTriggerEventList"
    r"""<p>The repository events that cause the trigger to run actions in another service, such as sending a notification through Amazon SNS. </p> <note> <p>The valid value \"all\" cannot be used with any other values.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryTrigger) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["destinationArn"] = value["destination_arn"]
    if "custom_data" in value:
        out["customData"] = value["custom_data"]
    if "branches" in value:
        import aws_sdk_codecommit.types.branch_name_list

        out["branches"] = (
            aws_sdk_codecommit.types.branch_name_list.serialize_aws_json_1_1(
                value["branches"]
            )
        )
    import aws_sdk_codecommit.types.repository_trigger_event_list

    out["events"] = (
        aws_sdk_codecommit.types.repository_trigger_event_list.serialize_aws_json_1_1(
            value["events"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RepositoryTrigger:
    out: RepositoryTrigger = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RepositoryTrigger.name required")
    if "destinationArn" in data:
        out["destination_arn"] = data["destinationArn"]
    else:
        raise DeserializationError("RepositoryTrigger.destination_arn required")
    if "customData" in data:
        out["custom_data"] = data["customData"]
    if "branches" in data:
        import aws_sdk_codecommit.types.branch_name_list

        out["branches"] = (
            aws_sdk_codecommit.types.branch_name_list.deserialize_aws_json_1_1(
                data["branches"]
            )
        )
    if "events" in data:
        import aws_sdk_codecommit.types.repository_trigger_event_list

        out["events"] = (
            aws_sdk_codecommit.types.repository_trigger_event_list.deserialize_aws_json_1_1(
                data["events"]
            )
        )
    else:
        raise DeserializationError("RepositoryTrigger.events required")
    return out
