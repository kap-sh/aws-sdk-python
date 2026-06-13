"""Generated from Smithy shape ``com.amazonaws.odb#ExadataIormConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_odb.types.db_iorm_config_list
    import aws_sdk_odb.types.iorm_lifecycle_state
    import aws_sdk_odb.types.objective


class ExadataIormConfig(TypedDict):
    db_plans: NotRequired["aws_sdk_odb.types.db_iorm_config_list.DbIormConfigList"]
    """<p>An array of IORM settings for all the database in the Exadata DB system.</p>"""
    lifecycle_details: NotRequired["str"]
    """<p>Additional information about the current lifecycleState.</p>"""
    lifecycle_state: NotRequired[
        "aws_sdk_odb.types.iorm_lifecycle_state.IormLifecycleState"
    ]
    """<p>The current state of IORM configuration for the Exadata DB system.</p>"""
    objective: NotRequired["aws_sdk_odb.types.objective.Objective"]
    """<p>The current value for the IORM objective. The default is AUTO.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExadataIormConfig) -> dict:
    out: dict = {}
    if "db_plans" in value:
        import aws_sdk_odb.types.db_iorm_config_list

        out["dbPlans"] = aws_sdk_odb.types.db_iorm_config_list.serialize_aws_json_1_0(
            value["db_plans"]
        )
    if "lifecycle_details" in value:
        out["lifecycleDetails"] = value["lifecycle_details"]
    if "lifecycle_state" in value:
        import aws_sdk_odb.types.iorm_lifecycle_state

        out["lifecycleState"] = (
            aws_sdk_odb.types.iorm_lifecycle_state.serialize_aws_json_1_0(
                value["lifecycle_state"]
            )
        )
    if "objective" in value:
        import aws_sdk_odb.types.objective

        out["objective"] = aws_sdk_odb.types.objective.serialize_aws_json_1_0(
            value["objective"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExadataIormConfig:
    out: ExadataIormConfig = {}  # type: ignore[typeddict-item]
    if "dbPlans" in data:
        import aws_sdk_odb.types.db_iorm_config_list

        out["db_plans"] = (
            aws_sdk_odb.types.db_iorm_config_list.deserialize_aws_json_1_0(
                data["dbPlans"]
            )
        )
    if "lifecycleDetails" in data:
        out["lifecycle_details"] = data["lifecycleDetails"]
    if "lifecycleState" in data:
        import aws_sdk_odb.types.iorm_lifecycle_state

        out["lifecycle_state"] = (
            aws_sdk_odb.types.iorm_lifecycle_state.deserialize_aws_json_1_0(
                data["lifecycleState"]
            )
        )
    if "objective" in data:
        import aws_sdk_odb.types.objective

        out["objective"] = aws_sdk_odb.types.objective.deserialize_aws_json_1_0(
            data["objective"]
        )
    return out
