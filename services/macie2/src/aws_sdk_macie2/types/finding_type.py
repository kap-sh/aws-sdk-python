"""Generated from Smithy shape ``com.amazonaws.macie2#FindingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The type of finding. For details about each type, see <a href=\"https://docs.aws.amazon.com/macie/latest/user/findings-types.html\">Types of findings</a> in the <i>Amazon Macie User Guide</i>. Possible values are:</p>"""
FindingType: TypeAlias = Literal[
    "SensitiveData:S3Object/Multiple",
    "SensitiveData:S3Object/Financial",
    "SensitiveData:S3Object/Personal",
    "SensitiveData:S3Object/Credentials",
    "SensitiveData:S3Object/CustomIdentifier",
    "Policy:IAMUser/S3BucketPublic",
    "Policy:IAMUser/S3BucketSharedExternally",
    "Policy:IAMUser/S3BucketReplicatedExternally",
    "Policy:IAMUser/S3BucketEncryptionDisabled",
    "Policy:IAMUser/S3BlockPublicAccessDisabled",
    "Policy:IAMUser/S3BucketSharedWithCloudFront",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SensitiveData:S3Object/Multiple",
        "SensitiveData:S3Object/Financial",
        "SensitiveData:S3Object/Personal",
        "SensitiveData:S3Object/Credentials",
        "SensitiveData:S3Object/CustomIdentifier",
        "Policy:IAMUser/S3BucketPublic",
        "Policy:IAMUser/S3BucketSharedExternally",
        "Policy:IAMUser/S3BucketReplicatedExternally",
        "Policy:IAMUser/S3BucketEncryptionDisabled",
        "Policy:IAMUser/S3BlockPublicAccessDisabled",
        "Policy:IAMUser/S3BucketSharedWithCloudFront",
    )
)


def serialize_json(value: FindingType) -> str:
    return value


def deserialize_json(data: str) -> FindingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FindingType value: {data!r}")
    return cast(FindingType, data)
