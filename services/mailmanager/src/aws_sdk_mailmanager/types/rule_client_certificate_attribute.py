"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleClientCertificateAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

"""<p>The client certificate attribute to evaluate in a rule condition. These attributes are extracted from the client certificate presented during mutual TLS authentication.</p>"""
RuleClientCertificateAttribute: TypeAlias = Literal[
    "CN",
    "SAN_RFC822_NAME",
    "SAN_DNS_NAME",
    "SAN_DIRECTORY_NAME",
    "SAN_UNIFORM_RESOURCE_IDENTIFIER",
    "SAN_IP_ADDRESS",
    "SAN_REGISTERED_ID",
    "SERIAL_NUMBER",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CN",
        "SAN_RFC822_NAME",
        "SAN_DNS_NAME",
        "SAN_DIRECTORY_NAME",
        "SAN_UNIFORM_RESOURCE_IDENTIFIER",
        "SAN_IP_ADDRESS",
        "SAN_REGISTERED_ID",
        "SERIAL_NUMBER",
    )
)


def serialize_aws_json_1_0(value: RuleClientCertificateAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleClientCertificateAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RuleClientCertificateAttribute value: {data!r}"
        )
    return cast(RuleClientCertificateAttribute, data)
