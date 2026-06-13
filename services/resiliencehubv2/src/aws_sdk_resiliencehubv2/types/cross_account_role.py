"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CrossAccountRole``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.iam_role_arn


class CrossAccountRole(TypedDict):
    cross_account_role_arn: "aws_sdk_resiliencehubv2.types.iam_role_arn.IamRoleArn"
    external_id: NotRequired["str"]
    """<p>The external ID used for assuming the cross-account role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrossAccountRole) -> dict:
    out: dict = {}
    out["crossAccountRoleArn"] = value["cross_account_role_arn"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    return out


def deserialize_json(data: dict) -> CrossAccountRole:
    out: CrossAccountRole = {}  # type: ignore[typeddict-item]
    if "crossAccountRoleArn" in data:
        out["cross_account_role_arn"] = data["crossAccountRoleArn"]
    else:
        raise DeserializationError("CrossAccountRole.cross_account_role_arn required")
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    return out
