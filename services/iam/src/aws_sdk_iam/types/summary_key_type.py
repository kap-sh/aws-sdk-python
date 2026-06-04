"""Generated from Smithy shape ``com.amazonaws.iam#summaryKeyType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

summaryKeyType: TypeAlias = Literal[
    "Users",
    "UsersQuota",
    "Groups",
    "GroupsQuota",
    "ServerCertificates",
    "ServerCertificatesQuota",
    "UserPolicySizeQuota",
    "GroupPolicySizeQuota",
    "GroupsPerUserQuota",
    "SigningCertificatesPerUserQuota",
    "AccessKeysPerUserQuota",
    "MFADevices",
    "MFADevicesInUse",
    "AccountMFAEnabled",
    "AccountAccessKeysPresent",
    "AccountPasswordPresent",
    "AccountSigningCertificatesPresent",
    "AttachedPoliciesPerGroupQuota",
    "AttachedPoliciesPerRoleQuota",
    "AttachedPoliciesPerUserQuota",
    "Policies",
    "PoliciesQuota",
    "PolicySizeQuota",
    "PolicyVersionsInUse",
    "PolicyVersionsInUseQuota",
    "VersionsPerPolicyQuota",
    "GlobalEndpointTokenVersion",
    "AssumeRolePolicySizeQuota",
    "InstanceProfiles",
    "InstanceProfilesQuota",
    "Providers",
    "RolePolicySizeQuota",
    "Roles",
    "RolesQuota",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Users",
        "UsersQuota",
        "Groups",
        "GroupsQuota",
        "ServerCertificates",
        "ServerCertificatesQuota",
        "UserPolicySizeQuota",
        "GroupPolicySizeQuota",
        "GroupsPerUserQuota",
        "SigningCertificatesPerUserQuota",
        "AccessKeysPerUserQuota",
        "MFADevices",
        "MFADevicesInUse",
        "AccountMFAEnabled",
        "AccountAccessKeysPresent",
        "AccountPasswordPresent",
        "AccountSigningCertificatesPresent",
        "AttachedPoliciesPerGroupQuota",
        "AttachedPoliciesPerRoleQuota",
        "AttachedPoliciesPerUserQuota",
        "Policies",
        "PoliciesQuota",
        "PolicySizeQuota",
        "PolicyVersionsInUse",
        "PolicyVersionsInUseQuota",
        "VersionsPerPolicyQuota",
        "GlobalEndpointTokenVersion",
        "AssumeRolePolicySizeQuota",
        "InstanceProfiles",
        "InstanceProfilesQuota",
        "Providers",
        "RolePolicySizeQuota",
        "Roles",
        "RolesQuota",
    )
)


def to_query_text(value: summaryKeyType) -> str:
    return value


def from_query_text(text: str) -> summaryKeyType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown summaryKeyType value: {text!r}")
    return cast(summaryKeyType, text)


def serialize_query(
    value: summaryKeyType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> summaryKeyType:
    return from_query_text(el.text or "")
