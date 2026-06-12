"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.aws_account_id
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.lens_arn
    import aws_sdk_wellarchitected.types.lens_description
    import aws_sdk_wellarchitected.types.lens_name
    import aws_sdk_wellarchitected.types.lens_status
    import aws_sdk_wellarchitected.types.lens_type
    import aws_sdk_wellarchitected.types.lens_version
    import aws_sdk_wellarchitected.types.timestamp


class LensSummary(TypedDict):
    lens_arn: NotRequired["aws_sdk_wellarchitected.types.lens_arn.LensArn"]
    """<p>The ARN of the lens.</p>"""
    lens_alias: NotRequired["aws_sdk_wellarchitected.types.lens_alias.LensAlias"]
    lens_name: NotRequired["aws_sdk_wellarchitected.types.lens_name.LensName"]
    lens_type: NotRequired["aws_sdk_wellarchitected.types.lens_type.LensType"]
    """<p>The type of the lens.</p>"""
    description: NotRequired[
        "aws_sdk_wellarchitected.types.lens_description.LensDescription"
    ]
    created_at: NotRequired["aws_sdk_wellarchitected.types.timestamp.Timestamp"]
    updated_at: NotRequired["aws_sdk_wellarchitected.types.timestamp.Timestamp"]
    lens_version: NotRequired["aws_sdk_wellarchitected.types.lens_version.LensVersion"]
    """<p>The version of the lens.</p>"""
    owner: NotRequired["aws_sdk_wellarchitected.types.aws_account_id.AwsAccountId"]
    lens_status: NotRequired["aws_sdk_wellarchitected.types.lens_status.LensStatus"]
    """<p>The status of the lens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LensSummary) -> dict:
    out: dict = {}
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "lens_alias" in value:
        out["LensAlias"] = value["lens_alias"]
    if "lens_name" in value:
        out["LensName"] = value["lens_name"]
    if "lens_type" in value:
        import aws_sdk_wellarchitected.types.lens_type

        out["LensType"] = aws_sdk_wellarchitected.types.lens_type.serialize_json(
            value["lens_type"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_wellarchitected.types.timestamp

        out["CreatedAt"] = aws_sdk_wellarchitected.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_wellarchitected.types.timestamp

        out["UpdatedAt"] = aws_sdk_wellarchitected.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "lens_version" in value:
        out["LensVersion"] = value["lens_version"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "lens_status" in value:
        import aws_sdk_wellarchitected.types.lens_status

        out["LensStatus"] = aws_sdk_wellarchitected.types.lens_status.serialize_json(
            value["lens_status"]
        )
    return out


def deserialize_json(data: dict) -> LensSummary:
    out: LensSummary = {}  # type: ignore[typeddict-item]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "LensAlias" in data:
        out["lens_alias"] = data["LensAlias"]
    if "LensName" in data:
        out["lens_name"] = data["LensName"]
    if "LensType" in data:
        import aws_sdk_wellarchitected.types.lens_type

        out["lens_type"] = aws_sdk_wellarchitected.types.lens_type.deserialize_json(
            data["LensType"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedAt" in data:
        import aws_sdk_wellarchitected.types.timestamp

        out["created_at"] = aws_sdk_wellarchitected.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_wellarchitected.types.timestamp

        out["updated_at"] = aws_sdk_wellarchitected.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "LensVersion" in data:
        out["lens_version"] = data["LensVersion"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "LensStatus" in data:
        import aws_sdk_wellarchitected.types.lens_status

        out["lens_status"] = aws_sdk_wellarchitected.types.lens_status.deserialize_json(
            data["LensStatus"]
        )
    return out
