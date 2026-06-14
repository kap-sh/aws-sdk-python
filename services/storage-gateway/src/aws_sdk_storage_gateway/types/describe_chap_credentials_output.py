"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeChapCredentialsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.chap_credentials


class DescribeChapCredentialsOutput(TypedDict):
    chap_credentials: NotRequired[
        "aws_sdk_storage_gateway.types.chap_credentials.ChapCredentials"
    ]
    """<p>An array of <a>ChapInfo</a> objects that represent CHAP credentials. Each object in the array contains CHAP credential information for one target-initiator pair. If no CHAP credentials are set, an empty array is returned. CHAP credential information is provided in a JSON object with the following fields:</p> <ul> <li> <p> <b>InitiatorName</b>: The iSCSI initiator that connects to the target.</p> </li> <li> <p> <b>SecretToAuthenticateInitiator</b>: The secret key that the initiator (for example, the Windows client) must provide to participate in mutual CHAP with the target.</p> </li> <li> <p> <b>SecretToAuthenticateTarget</b>: The secret key that the target must provide to participate in mutual CHAP with the initiator (e.g. Windows client).</p> </li> <li> <p> <b>TargetARN</b>: The Amazon Resource Name (ARN) of the storage volume.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeChapCredentialsOutput) -> dict:
    out: dict = {}
    if "chap_credentials" in value:
        import aws_sdk_storage_gateway.types.chap_credentials

        out["ChapCredentials"] = (
            aws_sdk_storage_gateway.types.chap_credentials.serialize_aws_json_1_1(
                value["chap_credentials"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeChapCredentialsOutput:
    out: DescribeChapCredentialsOutput = {}  # type: ignore[typeddict-item]
    if "ChapCredentials" in data:
        import aws_sdk_storage_gateway.types.chap_credentials

        out["chap_credentials"] = (
            aws_sdk_storage_gateway.types.chap_credentials.deserialize_aws_json_1_1(
                data["ChapCredentials"]
            )
        )
    return out
