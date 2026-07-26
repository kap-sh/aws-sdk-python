"""Generated from Smithy shape ``com.amazonaws.transfer#TestConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.connector_id
    import capo_transfer.types.message
    import capo_transfer.types.sftp_connector_connection_details
    import capo_transfer.types.status


class TestConnectionResponse(TypedDict, closed=True):
    connector_id: NotRequired["capo_transfer.types.connector_id.ConnectorId"]
    """<p>Returns the identifier of the connector object that you are testing.</p>"""
    status: NotRequired["capo_transfer.types.status.Status"]
    """<p>Returns <code>OK</code> for successful test, or <code>ERROR</code> if the test fails.</p>"""
    status_message: NotRequired["capo_transfer.types.message.Message"]
    """<p>Returns <code>Connection succeeded</code> if the test is successful. Or, returns a descriptive error message if the test fails. The following list provides troubleshooting details, depending on the error message that you receive.</p> <ul> <li> <p>Verify that your secret name aligns with the one in Transfer Role permissions.</p> </li> <li> <p>Verify the server URL in the connector configuration , and verify that the login credentials work successfully outside of the connector.</p> </li> <li> <p>Verify that the secret exists and is formatted correctly.</p> </li> <li> <p>Verify that the trusted host key in the connector configuration matches the <code>ssh-keyscan</code> output.</p> </li> </ul>"""
    sftp_connection_details: NotRequired[
        "capo_transfer.types.sftp_connector_connection_details.SftpConnectorConnectionDetails"
    ]
    """<p>Structure that contains the SFTP connector host key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestConnectionResponse) -> dict:
    out: dict = {}
    if "connector_id" in value:
        out["ConnectorId"] = value["connector_id"]
    if "status" in value:
        out["Status"] = value["status"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "sftp_connection_details" in value:
        import capo_transfer.types.sftp_connector_connection_details

        out["SftpConnectionDetails"] = (
            capo_transfer.types.sftp_connector_connection_details.serialize_aws_json_1_1(
                value["sftp_connection_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestConnectionResponse:
    out: TestConnectionResponse = {}  # type: ignore[typeddict-item]
    if "ConnectorId" in data:
        out["connector_id"] = data["ConnectorId"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "SftpConnectionDetails" in data:
        import capo_transfer.types.sftp_connector_connection_details

        out["sftp_connection_details"] = (
            capo_transfer.types.sftp_connector_connection_details.deserialize_aws_json_1_1(
                data["SftpConnectionDetails"]
            )
        )
    return out
