"""Generated from Smithy shape ``com.amazonaws.configservice#PutRetentionConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.retention_configuration


class PutRetentionConfigurationResponse(TypedDict, closed=True):
    retention_configuration: NotRequired[
        "capo_config_service.types.retention_configuration.RetentionConfiguration"
    ]
    """<p>Returns a retention configuration object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRetentionConfigurationResponse) -> dict:
    out: dict = {}
    if "retention_configuration" in value:
        import capo_config_service.types.retention_configuration

        out["RetentionConfiguration"] = (
            capo_config_service.types.retention_configuration.serialize_aws_json_1_1(
                value["retention_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRetentionConfigurationResponse:
    out: PutRetentionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "RetentionConfiguration" in data:
        import capo_config_service.types.retention_configuration

        out["retention_configuration"] = (
            capo_config_service.types.retention_configuration.deserialize_aws_json_1_1(
                data["RetentionConfiguration"]
            )
        )
    return out
