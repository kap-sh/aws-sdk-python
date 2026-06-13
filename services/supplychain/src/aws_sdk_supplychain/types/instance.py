"""Generated from Smithy shape ``com.amazonaws.supplychain#Instance``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_supplychain.types.aws_account_id
    import aws_sdk_supplychain.types.instance_description
    import aws_sdk_supplychain.types.instance_name
    import aws_sdk_supplychain.types.instance_state
    import aws_sdk_supplychain.types.instance_web_app_dns_domain
    import aws_sdk_supplychain.types.kms_key_arn
    import aws_sdk_supplychain.types.uuid


class Instance(TypedDict):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    aws_account_id: "aws_sdk_supplychain.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID that owns the instance.</p>"""
    state: "aws_sdk_supplychain.types.instance_state.InstanceState"
    """<p>The state of the instance.</p>"""
    error_message: NotRequired["str"]
    """<p>The Amazon Web Services Supply Chain instance error message. If the instance results in an unhealthy state, customers need to check the error message, delete the current instance, and recreate a new one based on the mitigation from the error message.</p>"""
    web_app_dns_domain: NotRequired[
        "aws_sdk_supplychain.types.instance_web_app_dns_domain.InstanceWebAppDnsDomain"
    ]
    """<p>The WebApp DNS domain name of the instance.</p>"""
    created_time: NotRequired["datetime.datetime"]
    """<p>The instance creation timestamp.</p>"""
    last_modified_time: NotRequired["datetime.datetime"]
    """<p>The instance last modified timestamp.</p>"""
    instance_name: NotRequired["aws_sdk_supplychain.types.instance_name.InstanceName"]
    """<p>The Amazon Web Services Supply Chain instance name.</p>"""
    instance_description: NotRequired[
        "aws_sdk_supplychain.types.instance_description.InstanceDescription"
    ]
    """<p>The Amazon Web Services Supply Chain instance description.</p>"""
    kms_key_arn: NotRequired["aws_sdk_supplychain.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you optionally provided for encryption. If you did not provide anything here, AWS Supply Chain uses the Amazon Web Services owned KMS key and nothing is returned.</p>"""
    version_number: NotRequired["float"]
    """<p>The version number of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Instance) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    out["awsAccountId"] = value["aws_account_id"]
    import aws_sdk_supplychain.types.instance_state

    out["state"] = aws_sdk_supplychain.types.instance_state.serialize_json(
        value["state"]
    )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "web_app_dns_domain" in value:
        out["webAppDnsDomain"] = value["web_app_dns_domain"]
    if "created_time" in value:
        import aws_sdk_supplychain.types._prelude.timestamp

        out["createdTime"] = (
            aws_sdk_supplychain.types._prelude.timestamp.serialize_json(
                value["created_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_supplychain.types._prelude.timestamp

        out["lastModifiedTime"] = (
            aws_sdk_supplychain.types._prelude.timestamp.serialize_json(
                value["last_modified_time"]
            )
        )
    if "instance_name" in value:
        out["instanceName"] = value["instance_name"]
    if "instance_description" in value:
        out["instanceDescription"] = value["instance_description"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "version_number" in value:
        out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> Instance:
    out: Instance = {}  # type: ignore[typeddict-item]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    else:
        raise DeserializationError("Instance.instance_id required")
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    else:
        raise DeserializationError("Instance.aws_account_id required")
    if "state" in data:
        import aws_sdk_supplychain.types.instance_state

        out["state"] = aws_sdk_supplychain.types.instance_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("Instance.state required")
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "webAppDnsDomain" in data:
        out["web_app_dns_domain"] = data["webAppDnsDomain"]
    if "createdTime" in data:
        import aws_sdk_supplychain.types._prelude.timestamp

        out["created_time"] = (
            aws_sdk_supplychain.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    if "lastModifiedTime" in data:
        import aws_sdk_supplychain.types._prelude.timestamp

        out["last_modified_time"] = (
            aws_sdk_supplychain.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    if "instanceDescription" in data:
        out["instance_description"] = data["instanceDescription"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "versionNumber" in data:
        out["version_number"] = data["versionNumber"]
    return out
