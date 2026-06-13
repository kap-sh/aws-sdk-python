"""Generated from Smithy shape ``com.amazonaws.backup#CreateRestoreTestingPlanInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.restore_testing_plan_for_create
    import aws_sdk_backup.types.sensitive_string_map


class CreateRestoreTestingPlanInput(TypedDict):
    creator_request_id: NotRequired["str"]
    """<p>This is a unique string that identifies the request and allows failed requests to be retriedwithout the risk of running the operation twice. This parameter is optional. If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>"""
    restore_testing_plan: "aws_sdk_backup.types.restore_testing_plan_for_create.RestoreTestingPlanForCreate"
    """<p>A restore testing plan must contain a unique <code>RestoreTestingPlanName</code> string you create and must contain a <code>ScheduleExpression</code> cron. You may optionally include a <code>StartWindowHours</code> integer and a <code>CreatorRequestId</code> string.</p> <p>The <code>RestoreTestingPlanName</code> is a unique string that is the name of the restore testing plan. This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.</p>"""
    tags: NotRequired["aws_sdk_backup.types.sensitive_string_map.SensitiveStringMap"]
    """<p>The tags to assign to the restore testing plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRestoreTestingPlanInput) -> dict:
    out: dict = {}
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    import aws_sdk_backup.types.restore_testing_plan_for_create

    out["RestoreTestingPlan"] = (
        aws_sdk_backup.types.restore_testing_plan_for_create.serialize_json(
            value["restore_testing_plan"]
        )
    )
    if "tags" in value:
        import aws_sdk_backup.types.sensitive_string_map

        out["Tags"] = aws_sdk_backup.types.sensitive_string_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateRestoreTestingPlanInput:
    out: CreateRestoreTestingPlanInput = {}  # type: ignore[typeddict-item]
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "RestoreTestingPlan" in data:
        import aws_sdk_backup.types.restore_testing_plan_for_create

        out["restore_testing_plan"] = (
            aws_sdk_backup.types.restore_testing_plan_for_create.deserialize_json(
                data["RestoreTestingPlan"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRestoreTestingPlanInput.restore_testing_plan required"
        )
    if "Tags" in data:
        import aws_sdk_backup.types.sensitive_string_map

        out["tags"] = aws_sdk_backup.types.sensitive_string_map.deserialize_json(
            data["Tags"]
        )
    return out
