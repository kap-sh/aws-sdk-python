"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeBatchDeleteConfigurationTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.batch_delete_configuration_task


class DescribeBatchDeleteConfigurationTaskResponse(TypedDict):
    task: NotRequired[
        "aws_sdk_application_discovery_service.types.batch_delete_configuration_task.BatchDeleteConfigurationTask"
    ]
    """<p> The <code>BatchDeleteConfigurationTask</code> that represents the deletion task being executed. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBatchDeleteConfigurationTaskResponse) -> dict:
    out: dict = {}
    if "task" in value:
        import aws_sdk_application_discovery_service.types.batch_delete_configuration_task

        out["task"] = (
            aws_sdk_application_discovery_service.types.batch_delete_configuration_task.serialize_aws_json_1_1(
                value["task"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeBatchDeleteConfigurationTaskResponse:
    out: DescribeBatchDeleteConfigurationTaskResponse = {}  # type: ignore[typeddict-item]
    if "task" in data:
        import aws_sdk_application_discovery_service.types.batch_delete_configuration_task

        out["task"] = (
            aws_sdk_application_discovery_service.types.batch_delete_configuration_task.deserialize_aws_json_1_1(
                data["task"]
            )
        )
    return out
