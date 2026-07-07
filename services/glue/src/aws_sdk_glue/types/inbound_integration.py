"""Generated from Smithy shape ``com.amazonaws.glue#InboundIntegration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.integration_config
    import aws_sdk_glue.types.integration_error_list
    import aws_sdk_glue.types.integration_status
    import aws_sdk_glue.types.integration_timestamp
    import aws_sdk_glue.types.string128
    import aws_sdk_glue.types.string512


class InboundIntegration(TypedDict, closed=True):
    source_arn: "aws_sdk_glue.types.string512.String512"
    """<p>The ARN of the source resource for the integration.</p>"""
    target_arn: "aws_sdk_glue.types.string512.String512"
    """<p>The ARN of the target resource for the integration.</p>"""
    integration_arn: "aws_sdk_glue.types.string128.String128"
    """<p>The ARN of the zero-ETL integration.</p>"""
    status: "aws_sdk_glue.types.integration_status.IntegrationStatus"
    """<p>The possible statuses are:</p> <ul> <li> <p>CREATING: The integration is being created.</p> </li> <li> <p>ACTIVE: The integration creation succeeds.</p> </li> <li> <p>MODIFYING: The integration is being modified.</p> </li> <li> <p>FAILED: The integration creation fails. </p> </li> <li> <p>DELETING: The integration is deleted.</p> </li> <li> <p>SYNCING: The integration is synchronizing.</p> </li> <li> <p>NEEDS_ATTENTION: The integration needs attention, such as synchronization.</p> </li> </ul>"""
    create_time: "aws_sdk_glue.types.integration_timestamp.IntegrationTimestamp"
    """<p>The time that the integration was created, in UTC.</p>"""
    integration_config: NotRequired[
        "aws_sdk_glue.types.integration_config.IntegrationConfig"
    ]
    """<p>Properties associated with the integration.</p>"""
    errors: NotRequired[
        "aws_sdk_glue.types.integration_error_list.IntegrationErrorList"
    ]
    """<p>A list of errors associated with the integration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InboundIntegration) -> dict:
    out: dict = {}
    out["SourceArn"] = value["source_arn"]
    out["TargetArn"] = value["target_arn"]
    out["IntegrationArn"] = value["integration_arn"]
    import aws_sdk_glue.types.integration_status

    out["Status"] = aws_sdk_glue.types.integration_status.serialize_aws_json_1_1(
        value["status"]
    )
    import aws_sdk_glue.types.integration_timestamp

    out["CreateTime"] = aws_sdk_glue.types.integration_timestamp.serialize_aws_json_1_1(
        value["create_time"]
    )
    if "integration_config" in value:
        import aws_sdk_glue.types.integration_config

        out["IntegrationConfig"] = (
            aws_sdk_glue.types.integration_config.serialize_aws_json_1_1(
                value["integration_config"]
            )
        )
    if "errors" in value:
        import aws_sdk_glue.types.integration_error_list

        out["Errors"] = (
            aws_sdk_glue.types.integration_error_list.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InboundIntegration:
    out: InboundIntegration = {}  # type: ignore[typeddict-item]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    else:
        raise DeserializationError("InboundIntegration.source_arn required")
    if "TargetArn" in data:
        out["target_arn"] = data["TargetArn"]
    else:
        raise DeserializationError("InboundIntegration.target_arn required")
    if "IntegrationArn" in data:
        out["integration_arn"] = data["IntegrationArn"]
    else:
        raise DeserializationError("InboundIntegration.integration_arn required")
    if "Status" in data:
        import aws_sdk_glue.types.integration_status

        out["status"] = aws_sdk_glue.types.integration_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    else:
        raise DeserializationError("InboundIntegration.status required")
    if "CreateTime" in data:
        import aws_sdk_glue.types.integration_timestamp

        out["create_time"] = (
            aws_sdk_glue.types.integration_timestamp.deserialize_aws_json_1_1(
                data["CreateTime"]
            )
        )
    else:
        raise DeserializationError("InboundIntegration.create_time required")
    if "IntegrationConfig" in data:
        import aws_sdk_glue.types.integration_config

        out["integration_config"] = (
            aws_sdk_glue.types.integration_config.deserialize_aws_json_1_1(
                data["IntegrationConfig"]
            )
        )
    if "Errors" in data:
        import aws_sdk_glue.types.integration_error_list

        out["errors"] = (
            aws_sdk_glue.types.integration_error_list.deserialize_aws_json_1_1(
                data["Errors"]
            )
        )
    return out
