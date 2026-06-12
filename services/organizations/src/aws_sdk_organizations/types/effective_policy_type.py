"""Generated from Smithy shape ``com.amazonaws.organizations#EffectivePolicyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

EffectivePolicyType: TypeAlias = Literal[
    "TAG_POLICY",
    "BACKUP_POLICY",
    "AISERVICES_OPT_OUT_POLICY",
    "CHATBOT_POLICY",
    "DECLARATIVE_POLICY_EC2",
    "SECURITYHUB_POLICY",
    "INSPECTOR_POLICY",
    "UPGRADE_ROLLOUT_POLICY",
    "BEDROCK_POLICY",
    "S3_POLICY",
    "NETWORK_SECURITY_DIRECTOR_POLICY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TAG_POLICY",
        "BACKUP_POLICY",
        "AISERVICES_OPT_OUT_POLICY",
        "CHATBOT_POLICY",
        "DECLARATIVE_POLICY_EC2",
        "SECURITYHUB_POLICY",
        "INSPECTOR_POLICY",
        "UPGRADE_ROLLOUT_POLICY",
        "BEDROCK_POLICY",
        "S3_POLICY",
        "NETWORK_SECURITY_DIRECTOR_POLICY",
    )
)


def serialize_aws_json_1_1(value: EffectivePolicyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EffectivePolicyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EffectivePolicyType value: {data!r}")
    return cast(EffectivePolicyType, data)
