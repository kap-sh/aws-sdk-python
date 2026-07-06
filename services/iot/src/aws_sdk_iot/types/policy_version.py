"""Generated from Smithy shape ``com.amazonaws.iot#PolicyVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.date_type
    import aws_sdk_iot.types.is_default_version
    import aws_sdk_iot.types.policy_version_id


class PolicyVersion(TypedDict, closed=True):
    version_id: NotRequired["aws_sdk_iot.types.policy_version_id.PolicyVersionId"]
    """<p>The policy version ID.</p>"""
    is_default_version: "aws_sdk_iot.types.is_default_version.IsDefaultVersion"
    """<p>Specifies whether the policy version is the default.</p>"""
    create_date: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The date and time the policy was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyVersion) -> dict:
    out: dict = {}
    if "version_id" in value:
        out["versionId"] = value["version_id"]
    out["isDefaultVersion"] = value.get("is_default_version", False)
    if "create_date" in value:
        import aws_sdk_iot.types.date_type

        out["createDate"] = aws_sdk_iot.types.date_type.serialize_json(
            value["create_date"]
        )
    return out


def deserialize_json(data: dict) -> PolicyVersion:
    out: PolicyVersion = {}  # type: ignore[typeddict-item]
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    if "isDefaultVersion" in data:
        out["is_default_version"] = data["isDefaultVersion"]
    else:
        out["is_default_version"] = False
    if "createDate" in data:
        import aws_sdk_iot.types.date_type

        out["create_date"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["createDate"]
        )
    return out
