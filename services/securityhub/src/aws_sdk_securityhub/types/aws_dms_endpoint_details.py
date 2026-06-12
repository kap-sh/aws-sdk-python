"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDmsEndpointDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsDmsEndpointDetails(TypedDict):
    certificate_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) for the SSL certificate that encrypts connections between the DMS endpoint and the replication instance. </p>"""
    database_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The name of the endpoint database.</p>"""
    endpoint_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the endpoint. </p>"""
    endpoint_identifier: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The database endpoint identifier. </p>"""
    endpoint_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The type of endpoint. Valid values are source and target. </p>"""
    engine_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The type of engine for the endpoint, depending on the <code>EndpointType</code> value. </p>"""
    external_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> A value that can be used for cross-account validation. </p>"""
    extra_connection_attributes: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Additional attributes associated with the connection. </p>"""
    kms_key_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> An DMS key identifier that is used to encrypt the connection parameters for the endpoint. If you don't specify a value for the <code>KmsKeyId</code> parameter, then DMS uses your default encryption key. KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.</p>"""
    port: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The port used to access the endpoint. </p>"""
    server_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The name of the server where the endpoint database resides.</p>"""
    ssl_mode: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The SSL mode used to connect to the endpoint. The default is none.</p>"""
    username: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The user name to be used to log in to the endpoint database. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDmsEndpointDetails) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    if "endpoint_identifier" in value:
        out["EndpointIdentifier"] = value["endpoint_identifier"]
    if "endpoint_type" in value:
        out["EndpointType"] = value["endpoint_type"]
    if "engine_name" in value:
        out["EngineName"] = value["engine_name"]
    if "external_id" in value:
        out["ExternalId"] = value["external_id"]
    if "extra_connection_attributes" in value:
        out["ExtraConnectionAttributes"] = value["extra_connection_attributes"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "port" in value:
        out["Port"] = value["port"]
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    if "ssl_mode" in value:
        out["SslMode"] = value["ssl_mode"]
    if "username" in value:
        out["Username"] = value["username"]
    return out


def deserialize_json(data: dict) -> AwsDmsEndpointDetails:
    out: AwsDmsEndpointDetails = {}  # type: ignore[typeddict-item]
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "EndpointArn" in data:
        out["endpoint_arn"] = data["EndpointArn"]
    if "EndpointIdentifier" in data:
        out["endpoint_identifier"] = data["EndpointIdentifier"]
    if "EndpointType" in data:
        out["endpoint_type"] = data["EndpointType"]
    if "EngineName" in data:
        out["engine_name"] = data["EngineName"]
    if "ExternalId" in data:
        out["external_id"] = data["ExternalId"]
    if "ExtraConnectionAttributes" in data:
        out["extra_connection_attributes"] = data["ExtraConnectionAttributes"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "ServerName" in data:
        out["server_name"] = data["ServerName"]
    if "SslMode" in data:
        out["ssl_mode"] = data["SslMode"]
    if "Username" in data:
        out["username"] = data["Username"]
    return out
