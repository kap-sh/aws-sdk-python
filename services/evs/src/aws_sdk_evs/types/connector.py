"""Generated from Smithy shape ``com.amazonaws.evs#Connector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_evs.types.appliance_fqdn
    import aws_sdk_evs.types.check_result
    import aws_sdk_evs.types.connector_id
    import aws_sdk_evs.types.connector_state
    import aws_sdk_evs.types.connector_type
    import aws_sdk_evs.types.connectors_checks_list
    import aws_sdk_evs.types.environment_id
    import aws_sdk_evs.types.secret_identifier
    import aws_sdk_evs.types.state_details


class Connector(TypedDict, closed=True):
    environment_id: NotRequired["aws_sdk_evs.types.environment_id.EnvironmentId"]
    """<p>The unique ID of the environment that the connector belongs to.</p>"""
    connector_id: NotRequired["aws_sdk_evs.types.connector_id.ConnectorId"]
    """<p>The unique ID of the connector.</p>"""
    type: NotRequired["aws_sdk_evs.types.connector_type.ConnectorType"]
    """<p>The type of the connector.</p>"""
    appliance_fqdn: NotRequired["aws_sdk_evs.types.appliance_fqdn.ApplianceFqdn"]
    """<p>The fully qualified domain name (FQDN) of the VCF appliance that the connector connects to.</p>"""
    secret_arn: NotRequired["aws_sdk_evs.types.secret_identifier.SecretIdentifier"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that stores the credentials for the VCF appliance.</p>"""
    state: NotRequired["aws_sdk_evs.types.connector_state.ConnectorState"]
    """<p>The state of the connector.</p>"""
    state_details: NotRequired["aws_sdk_evs.types.state_details.StateDetails"]
    """<p>A detailed description of the connector state.</p>"""
    status: NotRequired["aws_sdk_evs.types.check_result.CheckResult"]
    """<p>The status of the connector.</p>"""
    checks: NotRequired["aws_sdk_evs.types.connectors_checks_list.ConnectorsChecksList"]
    """<p>A list of checks that are run on the connector.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the connector was created.</p>"""
    modified_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the connector was modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Connector) -> dict:
    out: dict = {}
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "connector_id" in value:
        out["connectorId"] = value["connector_id"]
    if "type" in value:
        import aws_sdk_evs.types.connector_type

        out["type"] = aws_sdk_evs.types.connector_type.serialize_aws_json_1_0(
            value["type"]
        )
    if "appliance_fqdn" in value:
        out["applianceFqdn"] = value["appliance_fqdn"]
    if "secret_arn" in value:
        out["secretArn"] = value["secret_arn"]
    if "state" in value:
        import aws_sdk_evs.types.connector_state

        out["state"] = aws_sdk_evs.types.connector_state.serialize_aws_json_1_0(
            value["state"]
        )
    if "state_details" in value:
        out["stateDetails"] = value["state_details"]
    if "status" in value:
        import aws_sdk_evs.types.check_result

        out["status"] = aws_sdk_evs.types.check_result.serialize_aws_json_1_0(
            value["status"]
        )
    if "checks" in value:
        import aws_sdk_evs.types.connectors_checks_list

        out["checks"] = aws_sdk_evs.types.connectors_checks_list.serialize_aws_json_1_0(
            value["checks"]
        )
    if "created_at" in value:
        import aws_sdk_evs.types._prelude.timestamp

        out["createdAt"] = aws_sdk_evs.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "modified_at" in value:
        import aws_sdk_evs.types._prelude.timestamp

        out["modifiedAt"] = aws_sdk_evs.types._prelude.timestamp.serialize_aws_json_1_0(
            value["modified_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Connector:
    out: Connector = {}  # type: ignore[typeddict-item]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "connectorId" in data:
        out["connector_id"] = data["connectorId"]
    if "type" in data:
        import aws_sdk_evs.types.connector_type

        out["type"] = aws_sdk_evs.types.connector_type.deserialize_aws_json_1_0(
            data["type"]
        )
    if "applianceFqdn" in data:
        out["appliance_fqdn"] = data["applianceFqdn"]
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    if "state" in data:
        import aws_sdk_evs.types.connector_state

        out["state"] = aws_sdk_evs.types.connector_state.deserialize_aws_json_1_0(
            data["state"]
        )
    if "stateDetails" in data:
        out["state_details"] = data["stateDetails"]
    if "status" in data:
        import aws_sdk_evs.types.check_result

        out["status"] = aws_sdk_evs.types.check_result.deserialize_aws_json_1_0(
            data["status"]
        )
    if "checks" in data:
        import aws_sdk_evs.types.connectors_checks_list

        out["checks"] = (
            aws_sdk_evs.types.connectors_checks_list.deserialize_aws_json_1_0(
                data["checks"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_evs.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "modifiedAt" in data:
        import aws_sdk_evs.types._prelude.timestamp

        out["modified_at"] = (
            aws_sdk_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["modifiedAt"]
            )
        )
    return out
