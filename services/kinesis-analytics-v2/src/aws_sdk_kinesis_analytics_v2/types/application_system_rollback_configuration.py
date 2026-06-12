"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationSystemRollbackConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.boolean_object


class ApplicationSystemRollbackConfiguration(TypedDict):
    rollback_enabled: "aws_sdk_kinesis_analytics_v2.types.boolean_object.BooleanObject"
    """<p>Describes whether system rollbacks are enabled for a Managed Service for Apache Flink application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSystemRollbackConfiguration) -> dict:
    out: dict = {}
    out["RollbackEnabled"] = value["rollback_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationSystemRollbackConfiguration:
    out: ApplicationSystemRollbackConfiguration = {}  # type: ignore[typeddict-item]
    if "RollbackEnabled" in data:
        out["rollback_enabled"] = data["RollbackEnabled"]
    else:
        raise DeserializationError(
            "ApplicationSystemRollbackConfiguration.rollback_enabled required"
        )
    return out
