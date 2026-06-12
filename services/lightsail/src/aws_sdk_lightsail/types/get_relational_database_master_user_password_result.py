"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseMasterUserPasswordResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.sensitive_string


class GetRelationalDatabaseMasterUserPasswordResult(TypedDict):
    master_user_password: NotRequired[
        "aws_sdk_lightsail.types.sensitive_string.SensitiveString"
    ]
    """<p>The master user password for the <code>password version</code> specified.</p>"""
    created_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the specified version of the master user password was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetRelationalDatabaseMasterUserPasswordResult,
) -> dict:
    out: dict = {}
    if "master_user_password" in value:
        out["masterUserPassword"] = value["master_user_password"]
    if "created_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["createdAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetRelationalDatabaseMasterUserPasswordResult:
    out: GetRelationalDatabaseMasterUserPasswordResult = {}  # type: ignore[typeddict-item]
    if "masterUserPassword" in data:
        out["master_user_password"] = data["masterUserPassword"]
    if "createdAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["created_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    return out
