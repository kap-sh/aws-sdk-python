"""Generated from Smithy shape ``com.amazonaws.iam#summaryKeyType``."""

from typing import Literal, TypeAlias, cast

from capo_iam._protocol.xml import Element

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
def to_query_text(value: summaryKeyType) -> str:
    return value


def from_query_text(text: str) -> summaryKeyType:
    return cast(summaryKeyType, text)


def serialize_query(
    value: summaryKeyType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> summaryKeyType:
    return from_query_text(el.text or "")
