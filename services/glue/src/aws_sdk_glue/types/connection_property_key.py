"""Generated from Smithy shape ``com.amazonaws.glue#ConnectionPropertyKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ConnectionPropertyKey: TypeAlias = Literal[
    "HOST",
    "PORT",
    "USERNAME",
    "PASSWORD",
    "ENCRYPTED_PASSWORD",
    "JDBC_DRIVER_JAR_URI",
    "JDBC_DRIVER_CLASS_NAME",
    "JDBC_ENGINE",
    "JDBC_ENGINE_VERSION",
    "CONFIG_FILES",
    "INSTANCE_ID",
    "JDBC_CONNECTION_URL",
    "JDBC_ENFORCE_SSL",
    "CUSTOM_JDBC_CERT",
    "SKIP_CUSTOM_JDBC_CERT_VALIDATION",
    "CUSTOM_JDBC_CERT_STRING",
    "CONNECTION_URL",
    "KAFKA_BOOTSTRAP_SERVERS",
    "KAFKA_SSL_ENABLED",
    "KAFKA_CUSTOM_CERT",
    "KAFKA_SKIP_CUSTOM_CERT_VALIDATION",
    "KAFKA_CLIENT_KEYSTORE",
    "KAFKA_CLIENT_KEYSTORE_PASSWORD",
    "KAFKA_CLIENT_KEY_PASSWORD",
    "ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD",
    "ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD",
    "KAFKA_SASL_MECHANISM",
    "KAFKA_SASL_PLAIN_USERNAME",
    "KAFKA_SASL_PLAIN_PASSWORD",
    "ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD",
    "KAFKA_SASL_SCRAM_USERNAME",
    "KAFKA_SASL_SCRAM_PASSWORD",
    "KAFKA_SASL_SCRAM_SECRETS_ARN",
    "ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD",
    "KAFKA_SASL_GSSAPI_KEYTAB",
    "KAFKA_SASL_GSSAPI_KRB5_CONF",
    "KAFKA_SASL_GSSAPI_SERVICE",
    "KAFKA_SASL_GSSAPI_PRINCIPAL",
    "SECRET_ID",
    "CONNECTOR_URL",
    "CONNECTOR_TYPE",
    "CONNECTOR_CLASS_NAME",
    "ENDPOINT",
    "ENDPOINT_TYPE",
    "ROLE_ARN",
    "REGION",
    "WORKGROUP_NAME",
    "CLUSTER_IDENTIFIER",
    "DATABASE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HOST",
        "PORT",
        "USERNAME",
        "PASSWORD",
        "ENCRYPTED_PASSWORD",
        "JDBC_DRIVER_JAR_URI",
        "JDBC_DRIVER_CLASS_NAME",
        "JDBC_ENGINE",
        "JDBC_ENGINE_VERSION",
        "CONFIG_FILES",
        "INSTANCE_ID",
        "JDBC_CONNECTION_URL",
        "JDBC_ENFORCE_SSL",
        "CUSTOM_JDBC_CERT",
        "SKIP_CUSTOM_JDBC_CERT_VALIDATION",
        "CUSTOM_JDBC_CERT_STRING",
        "CONNECTION_URL",
        "KAFKA_BOOTSTRAP_SERVERS",
        "KAFKA_SSL_ENABLED",
        "KAFKA_CUSTOM_CERT",
        "KAFKA_SKIP_CUSTOM_CERT_VALIDATION",
        "KAFKA_CLIENT_KEYSTORE",
        "KAFKA_CLIENT_KEYSTORE_PASSWORD",
        "KAFKA_CLIENT_KEY_PASSWORD",
        "ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD",
        "ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD",
        "KAFKA_SASL_MECHANISM",
        "KAFKA_SASL_PLAIN_USERNAME",
        "KAFKA_SASL_PLAIN_PASSWORD",
        "ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD",
        "KAFKA_SASL_SCRAM_USERNAME",
        "KAFKA_SASL_SCRAM_PASSWORD",
        "KAFKA_SASL_SCRAM_SECRETS_ARN",
        "ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD",
        "KAFKA_SASL_GSSAPI_KEYTAB",
        "KAFKA_SASL_GSSAPI_KRB5_CONF",
        "KAFKA_SASL_GSSAPI_SERVICE",
        "KAFKA_SASL_GSSAPI_PRINCIPAL",
        "SECRET_ID",
        "CONNECTOR_URL",
        "CONNECTOR_TYPE",
        "CONNECTOR_CLASS_NAME",
        "ENDPOINT",
        "ENDPOINT_TYPE",
        "ROLE_ARN",
        "REGION",
        "WORKGROUP_NAME",
        "CLUSTER_IDENTIFIER",
        "DATABASE",
    )
)


def serialize_aws_json_1_1(value: ConnectionPropertyKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionPropertyKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionPropertyKey value: {data!r}")
    return cast(ConnectionPropertyKey, data)
